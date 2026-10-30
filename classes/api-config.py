class ApiConfig:
    def __init__(self, api_key, model="gpt-3.5-turbo", max_tokens=100):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.base_url = "https://api.openai.com/v1"
        
dev_config = ApiConfig("api-key-value", max_tokens=50)

prod_config = ApiConfig("api-key-value", model="gpt-4", max_tokens=100)

print(f"Dev Config: API Key: {dev_config.api_key}, Model: {dev_config.model}, Max Tokens: {dev_config.max_tokens}")
print(f"Prod Config: API Key: {prod_config.api_key}, Model: {prod_config.model}, Max Tokens: {prod_config.max_tokens}")
print(f"Dev Base URL: {dev_config.base_url}")