# kingpick_api_client.AuthApi

All URIs are relative to *https://kingpick-admin-api.endpoints.ciandt-cognitive-sandbox.cloud.goog/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**token**](AuthApi.md#token) | **GET** /auth/token | 


# **token**
> str token()



Generate a new authentication token

### Example 
```python
from __future__ import print_statement
import time
import kingpick_api_client
from kingpick_api_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: google_id_token
kingpick_api_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = kingpick_api_client.AuthApi()

try: 
    api_response = api_instance.token()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[google_id_token](../README.md#google_id_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

