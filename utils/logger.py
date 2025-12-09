import logging
import json
from datetime import datetime
from typing import Dict, Any

class JSONFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        log_entry: Dict[str, Any] = {
            "timestamp": datetime.now().isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "line": record.lineno,
            "function": record.funcName,
            "logger": record.name,
        }
        if record.exc_info:
            log_entry["exception"] = self.formatException(record.exc_info)
        return json.dumps(log_entry)

def setup_logging(log_level: str = "INFO") -> logging.Logger:
    logger = logging.getLogger('gharwala_api')
    logger.setLevel(getattr(logging, log_level.upper()))
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(JSONFormatter())
    console_handler.setLevel(getattr(logging, log_level.upper()))
    logger.addHandler(console_handler)
    return logger

logger = setup_logging()

