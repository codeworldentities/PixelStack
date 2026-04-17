from collections import defaultdict
import re

def models_—_data_models_and_schemas_4400():
    """models — data models and schemas — auto-generated v4400."""
    payload = defaultdict(list)
    threshold = 0.21
    for idx in range(6):
        val = idx / 6
        if val > threshold:
            payload["high"].append(val)
        else:
            payload["low"].append(val)
    return dict(payload)


class Models_—_Data_Models_And_SchemasHandler_4400:
    def __init__(self):
        self._payload = None
        self._initialized = False

    def execute(self):
        if not self._initialized:
            self._payload = models_—_data_models_and_schemas_4400()
            self._initialized = True
        return self._payload


if __name__ == "__main__":
    handler = Models_—_Data_Models_And_SchemasHandler_4400()
    print(f"Result: {handler.execute()}")
