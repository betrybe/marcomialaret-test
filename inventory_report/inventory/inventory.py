from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(cls, path_file, report_type):
        ext = path_file.split('.')[1]
        if ext == "csv":
            data = CsvImporter().import_data(path_file)
        
    @classmethod
    def generate(cls, data, report_type):
        if report_type == "simples":
            return SimpleReport.generate(data)
        return CompleteReport.generate(data)
