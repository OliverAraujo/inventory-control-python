import contextlib
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from inventory import register_product, record_entry, record_issue
from storage import load_inventory, save_inventory
from main import main


class InventoryTests(unittest.TestCase):
    def test_stock_workflow(self):
        products = {}
        register_product(products, " Mouse ", 10)
        record_entry(products, "MOUSE", 5)
        record_issue(products, "mouse", 3)
        self.assertEqual(products, {"mouse": 12})

    def test_duplicates_and_empty_names(self):
        products = {"mouse": 10}
        for name in [" MOUSE ", "", "  "]:
            with self.subTest(name=name), self.assertRaises(ValueError):
                register_product(products, name, 1)
        self.assertEqual(products, {"mouse": 10})

    def test_invalid_quantities_do_not_mutate(self):
        for operation in [register_product, record_entry, record_issue]:
            for quantity in [-1, 1.5, True, "2"]:
                products = {"mouse": 10}
                with self.subTest(operation=operation, quantity=quantity), self.assertRaises(ValueError):
                    operation(products, "keyboard" if operation is register_product else "mouse", quantity)
                self.assertEqual(products, {"mouse": 10})

    def test_zero_initial_stock_and_positive_movements(self):
        products = {}
        register_product(products, "mouse", 0)
        for operation in [record_entry, record_issue]:
            with self.assertRaises(ValueError):
                operation(products, "mouse", 0)
        self.assertEqual(products["mouse"], 0)

    def test_unknown_product(self):
        for operation in [record_entry, record_issue]:
            with self.assertRaises(ValueError):
                operation({}, "mouse", 1)

    def test_insufficient_stock_and_exact_withdrawal(self):
        products = {"mouse": 3}
        with self.assertRaises(ValueError):
            record_issue(products, "mouse", 4)
        self.assertEqual(products["mouse"], 3)
        record_issue(products, "mouse", 3)
        self.assertEqual(products["mouse"], 0)

    def test_round_trip_and_missing_file(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "data" / "inventory.json"
            self.assertEqual(load_inventory(path), {})
            save_inventory({"café": 7}, path)
            self.assertEqual(load_inventory(path), {"café": 7})

    def test_corrupt_or_invalid_files_stop_without_overwrite(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "inventory.json"
            for content in ['broken json', '[]', '{"mouse": -1}', '{"Mouse": 2}', '{"mouse": true}']:
                path.write_text(content, encoding="utf-8")
                with self.subTest(content=content), contextlib.redirect_stdout(io.StringIO()):
                    self.assertEqual(main(path), 1)
                self.assertEqual(path.read_text(encoding="utf-8"), content)

    def test_failed_replace_preserves_existing_file(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "inventory.json"
            save_inventory({"mouse": 10}, path)
            with patch("storage.os.replace", side_effect=OSError("disk failure")):
                with self.assertRaises(OSError):
                    save_inventory({"mouse": 99}, path)
            self.assertEqual(load_inventory(path), {"mouse": 10})
            self.assertEqual(len(list(Path(folder).iterdir())), 1)

    def test_cli_workflow_and_restart(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "inventory.json"
            answers = ["Y", "1", "mouse", "10", "2", "mouse", "5", "3", "mouse", "3", "4", "5"]
            output = io.StringIO()
            with patch("builtins.input", side_effect=answers), contextlib.redirect_stdout(output):
                self.assertEqual(main(path), 0)
            self.assertIn("mouse: 12 unit(s)", output.getvalue())
            with patch("builtins.input", side_effect=["Y", "4", "5"]), contextlib.redirect_stdout(output):
                self.assertEqual(main(path), 0)
            self.assertEqual(load_inventory(path), {"mouse": 12})

    def test_cli_save_failure_does_not_change_active_stock(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "inventory.json"
            save_inventory({"mouse": 10}, path)
            output = io.StringIO()
            with patch("builtins.input", side_effect=["Y", "2", "mouse", "5", "4", "5"]), patch("main.save_inventory", side_effect=OSError("disk full")), contextlib.redirect_stdout(output):
                self.assertEqual(main(path), 0)
            self.assertIn("mouse: 10 unit(s)", output.getvalue())
            self.assertEqual(load_inventory(path), {"mouse": 10})


if __name__ == "__main__":
    unittest.main()
