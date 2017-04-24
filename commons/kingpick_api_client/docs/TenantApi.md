# kingpick_api_client.TenantApi

All URIs are relative to *https://kingpick-admin-api.endpoints.ciandt-cognitive-sandbox.cloud.goog/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tenant**](TenantApi.md#get_tenant) | **GET** /tenants/{tenant_id} | 
[**get_tenants**](TenantApi.md#get_tenants) | **GET** /tenants | 
[**post_tenant**](TenantApi.md#post_tenant) | **POST** /tenants | 
[**put_tenant**](TenantApi.md#put_tenant) | **PUT** /tenants/{tenant_id} | 


# **get_tenant**
> Tenant get_tenant(tenant_id)



get a specific tenant

### Example 
```python
from __future__ import print_statement
import time
import kingpick_api_client
from kingpick_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kingpick_api_client.TenantApi()
tenant_id = 'tenant_id_example' # str | tenant id

try: 
    api_response = api_instance.get_tenant(tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantApi->get_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| tenant id | 

### Return type

[**Tenant**](Tenant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenants**
> Tenants get_tenants()



List all tenants

### Example 
```python
from __future__ import print_statement
import time
import kingpick_api_client
from kingpick_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kingpick_api_client.TenantApi()

try: 
    api_response = api_instance.get_tenants()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantApi->get_tenants: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Tenants**](Tenants.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tenant**
> Tenant post_tenant(tenant)



Creates a new tenant

### Example 
```python
from __future__ import print_statement
import time
import kingpick_api_client
from kingpick_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kingpick_api_client.TenantApi()
tenant = kingpick_api_client.Tenant() # Tenant | Tenant to create

try: 
    api_response = api_instance.post_tenant(tenant)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantApi->post_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant** | [**Tenant**](Tenant.md)| Tenant to create | 

### Return type

[**Tenant**](Tenant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_tenant**
> Tenant put_tenant(tenant_id, tenant)



updates a tenant

### Example 
```python
from __future__ import print_statement
import time
import kingpick_api_client
from kingpick_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kingpick_api_client.TenantApi()
tenant_id = 'tenant_id_example' # str | tenant id
tenant = kingpick_api_client.Tenant() # Tenant | Tenant to update

try: 
    api_response = api_instance.put_tenant(tenant_id, tenant)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantApi->put_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| tenant id | 
 **tenant** | [**Tenant**](Tenant.md)| Tenant to update | 

### Return type

[**Tenant**](Tenant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

