from typing import List

from report_monaco import Racer, RacingDataAnalyzer, read_files, validate_path

from web_report.constants import FOLDER


class Analyze:

    @property
    def run_analyzer(self) -> RacingDataAnalyzer:
        folder_path = validate_path(FOLDER)
        raw_data = read_files(folder_path)
        analyzer = RacingDataAnalyzer(raw_data)
        analyzer.build_report()
        return analyzer

    def sort(self, direction: bool) -> List[Racer]:
        analyzer = self.run_analyzer
        analyzer.sort_by_time(direction=direction)
        return analyzer.enumerate_drivers()

    def find_code(self, code) -> List[Racer]:
        return self.run_analyzer.find_driver_by_code(driver_code=code)
