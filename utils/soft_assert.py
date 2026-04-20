import logging


class SoftAssert:
    def __init__(self, logger_name="Logger"):
        self.errors = []
        self.logger = logging.getLogger(logger_name)

    def __call__(self, condition, message):
        if not condition:
            self.errors.append(message)
            self.logger.error(f"[SOFT ASSERT FAIL] {message}")

    def finalize(self):
        if self.errors:
            self.logger.error("=== SOFT ASSERT SUMMARY ===")
            for error in self.errors:
                self.logger.error(error)

            raise AssertionError("\n".join(self.errors))
