def error_return(status: int, message: str) -> tuple:
    data = {
        "error": {
            "reason": message,
        }
    }
    return data, status, {"Content-Type": "application/json"}
