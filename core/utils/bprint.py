from datetime import datetime

from core.utils.color import ColorUtils


class PrintUtils:
    @classmethod
    def get_date(cls):
        return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    @classmethod
    def print_with_date(cls, string):
        print(f"[{PrintUtils.get_date()}] {string}")

    @classmethod
    def print_with_date_success(cls, string):
        cls.print_with_date(f"{ColorUtils.OKGREEN}{string} ⚡️{ColorUtils.ENDC}")

    @classmethod
    def print_with_date_warning(cls, string):
        cls.print_with_date(f"{ColorUtils.WARNING}{string} ⚠️️{ColorUtils.ENDC}")

    @classmethod
    def print_with_date_info(cls, string):
        cls.print_with_date(f"{ColorUtils.OKBLUE}{string} 📚{ColorUtils.ENDC}")

    @classmethod
    def print_with_date_error(cls, string):
        cls.print_with_date(f"{ColorUtils.FAIL}{string} 😡{ColorUtils.ENDC}")
