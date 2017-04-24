# kingpick_api_client.ProjectApi

All URIs are relative to *https://kingpick-admin-api.endpoints.ciandt-cognitive-sandbox.cloud.goog/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project**](ProjectApi.md#create_project) | **POST** /projects | Creates a new project
[**get_project**](ProjectApi.md#get_project) | **GET** /projects/{project_id} | 
[**list_projects**](ProjectApi.md#list_projects) | **GET** /projects | 
[**put_project**](ProjectApi.md#put_project) | **PUT** /projects/{project_id} | 


# **create_project**
> Project create_project(tenant_id, project)

Creates a new project

Creates a new project return the project.

### Example 
```python
from __future__ import print_statement
import time
import kingpick_api_client
from kingpick_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kingpick_api_client.ProjectApi()
tenant_id = 'tenant_id_example' # str | tenant id
project = kingpick_api_client.Project() # Project | Project to create

try: 
    # Creates a new project
    api_response = api_instance.create_project(tenant_id, project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| tenant id | 
 **project** | [**Project**](Project.md)| Project to create | 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> Project get_project(tenant_id, project_id)



get a specific project

### Example 
```python
from __future__ import print_statement
import time
import kingpick_api_client
from kingpick_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kingpick_api_client.ProjectApi()
tenant_id = 'tenant_id_example' # str | tenant id
project_id = 'project_id_example' # str | project id

try: 
    api_response = api_instance.get_project(tenant_id, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| tenant id | 
 **project_id** | **str**| project id | 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_projects**
> Projects list_projects(tenant_id)



List all projects

### Example 
```python
from __future__ import print_statement
import time
import kingpick_api_client
from kingpick_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kingpick_api_client.ProjectApi()
tenant_id = 'tenant_id_example' # str | tenant id

try: 
    api_response = api_instance.list_projects(tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->list_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| tenant id | 

### Return type

[**Projects**](Projects.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_project**
> Project put_project(tenant_id, project_id, project)



updates a project

### Example 
```python
from __future__ import print_statement
import time
import kingpick_api_client
from kingpick_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kingpick_api_client.ProjectApi()
tenant_id = 'tenant_id_example' # str | tenant id
project_id = 'project_id_example' # str | project id
project = kingpick_api_client.Project() # Project | Project to update

try: 
    api_response = api_instance.put_project(tenant_id, project_id, project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->put_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| tenant id | 
 **project_id** | **str**| project id | 
 **project** | [**Project**](Project.md)| Project to update | 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

