# kingpick_api_client.DefaultApi

All URIs are relative to *https://kingpick-admin-api.endpoints.ciandt-cognitive-sandbox.cloud.goog/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**setup**](DefaultApi.md#setup) | **POST** /setup | 


# **setup**
> setup()



Setup basic infrastructure

### Example 
```python
from __future__ import print_statement
import time
import kingpick_api_client
from kingpick_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kingpick_api_client.DefaultApi()

try: 
    api_instance.setup()
except ApiException as e:
    print("Exception when calling DefaultApi->setup: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

