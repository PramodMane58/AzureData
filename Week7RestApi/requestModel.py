import requests
import os
import json
import base64
import adal

def GetAccessToken(tenant,client_id,client_secret):
    url = 'https://login.microsoftonline.com/' + tenant + '/oauth2/token'
    data = {'grant_type': 'client_credentials', 'client_id': client_id,
            'client_secret': client_secret}
    r = requests.post(url, data)
    return r.json()

def CreateResourceGroups(subscriptionId,resourceGroupName,apiversion,headers):
    url = 'https://management.azure.com/subscriptions/' + subscriptionId + '/resourcegroups/' + resourceGroupName
    body = {"location":'centralus'}
    r = requests.put(url,data = json.dumps(body), headers=headers, params={'api-version': apiversion})
    return r.json()

def CreateDatabricksWorkspace(subscriptionId,resourceGroupName,workspaceName,apiversion,headers):
    url = 'https://management.azure.com/subscriptions/' + subscriptionId + '/resourceGroups/' + resourceGroupName + '/providers/Microsoft.Databricks/workspaces/' + workspaceName
    body = {'location': 'centralus', "properties": {
        "managedResourceGroupId": '/subscriptions/' + subscriptionId + '/resourceGroups/apiatabriks'}}
    r = requests.put(url,data=json.dumps(body), headers=headers, params={'api-version': apiversion})
    return r.json()

def CreateDatabricksToken(domain,token):
    response = requests.post(
        'https://%s/api/2.0/token/create' % (domain),
        headers={'Authorization': b"Basic " + base64.standard_b64encode(b"token:" + str.encode(token))},
      json={
        "lifetime_seconds": 10000,
        "comment": "this is an example token"
        }
    )
    print(response)
    if response.status_code == 200:
        return response.json()
    #else:
        #return "Error launching cluster: %s: %s" % (response.json()["error_code"], response.json()["message"])


def CreateClustar(domain,token,clusterName,numWorkers):
    response = requests.post(
        'https://%s/api/2.0/clusters/create' % (domain),
        headers={'Authorization': b"Basic " + base64.standard_b64encode(b"token:" + token)},
        json={
            "cluster_name": clusterName,
            "spark_version": "5.3.x-scala2.11",
            "node_type_id": "Standard_DS3_v2",
            "spark_conf": {
                "spark.speculation": True
            },
            "num_workers": numWorkers
        }
    )
    if response.status_code == 200:
        return  response.json()
    else:
        return  "Error launching cluster: %s: %s" % (response.json()["error_code"], response.json()["message"])

def ImportNotebook(domain,token,sourcefilePath,destinationpath):
    '''
    response = requests.post(
        'https://' + domain + '/api/2.0/dbfs/create',
        headers={'Authorization': b"Basic " + base64.standard_b64encode(b"token:" + token)},
        json={"path": "/temp/upload_large_file", "overwrite": "true"}
    )
    handle = response.json()['handle']
    '''
    f = open(sourcefilePath, "r")
    file = base64.standard_b64encode(f.read().encode()).decode("utf-8")

    '''
    response = requests.post(
        'https://' + domain + '/api/2.0/dbfs/add-block',
        headers={'Authorization': b"Basic " + base64.standard_b64encode(b"token:" + token)},
        json={"handle": handle, "data": file}
    )
    '''
    # json_data = json.dumps(file)

    response = requests.post(
        'https://%s/api/2.0/workspace/import' % (domain),
        headers={'Authorization': b"Basic " + base64.standard_b64encode(b"token:" + token)},
        json={
            "content": file,
            "path": destinationpath,
            "language": "PYTHON",
            "overwrite": False,
            "format": "SOURCE"
        }
    )
    return response

def Addlibraries(domain,token,clusterid):
    response = requests.post('https://%s/api/2.0/libraries/install' % (domain),
    headers={'Authorization': b"Basic " + base64.standard_b64encode(b"token:" + token)},
    json={
    "cluster_id": clusterid,
    "libraries":[
    {
    "pypi": {
    "package": "nltk==3.4.3"
    }},{
    "pypi": {
    #"package": "nltk==3.4.3"
    "package": "pickle"
    #"repo": "http://my-pypi-mirror.com"
    }},{
    "pypi": {
            "package": "re"
    }},{
    "pypi": {
            "package": "pandas"
        }},{
    "pypi": {
            "package": "azure"
    }},{
    "pypi": {
            "package": "sklearn"
        },
    },{
    "pypi": {
            "package": "azure.cosmos"
    }}]
    }
    )
    print(response.status_code)

def CreateStorageaccount(subscriptionId,resourceGroupName,accountName,headers,apiVersion):
    url="https://management.azure.com/subscriptions/"+subscriptionId+"/resourceGroups/"+resourceGroupName+"/providers/Microsoft.Storage/storageAccounts/"+accountName+"?api-version="+apiVersion
    body={
            "sku": {
                "name": "Standard_GRS"
            },
            "kind": "StorageV2",
            "location": "centralus",
        }
    response = requests.put(url,data=json.dumps(body),headers=headers)
    return response

def CreateDataFactory(subscriptionId,resourceGroupName,dataFactoryName,headers,apiVersion):
    url = "https://management.azure.com/subscriptions/" + subscriptionId + "/resourceGroups/" + resourceGroupName + "/providers/Microsoft.DataFactory/factories/" + dataFactoryName + "?api-version="+apiVersion
    body = {
        "name": dataFactoryName,
        "location": "centralus",
        #"properties": {
        #    "provisioningState": "Succeeded",
        #    "loggingStorageAccountKey": "**********",
        #    "createTime": "2017-09-14T06:22:59.9106216Z",
        #    "version": "2018-06-01"
        #},
        #"identity": {
        #    "type": "SystemAssigned",
        #    "principalId": "<service principal ID>",
        #    "tenantId": "<tenant ID>"
        #},
        #"id": "dataFactoryName",
        #"type": "Microsoft.DataFactory/factories",
    }
    response =requests.put(url, data=json.dumps(body), headers=headers)
    print(response.json())
    return response

def CreatedabriksLinkedServices(subscriptionId,resourceGroupName,dataFactoryName,linkedServiceName,accessToken,domain,clusterid,headers):
    url = "https://management.azure.com/subscriptions/"+subscriptionId+"/resourceGroups/"+resourceGroupName+"/providers/Microsoft.DataFactory/factories/"+dataFactoryName+"/linkedservices/"+linkedServiceName+"?api-version=2018-06-01"
    body ={"properties": {
        "description" : "train model notebook",
        "type": "AzureDatabricks",
        "typeProperties": {
            "accessToken": accessToken,
            "domain" : "https://"+domain,
            "existingClusterId" : clusterid
        }
    }
    }
    response = requests.put(url, data=json.dumps(body), headers=headers)
    print(response.json())
    return response


def CreatePipelines(subscriptionId,resourceGroupName,dataFactoryName,pipelineName,linkedServiceName,notebookPath,headers):
    print("Starting Pipe Line")
    url =  "https://management.azure.com/subscriptions/"+ subscriptionId +"/resourceGroups/"+resourceGroupName +"/providers/Microsoft.DataFactory/factories/"+ dataFactoryName+"/pipelines/"+ pipelineName+"?api-version=2018-06-01"
    body = {
        "name": pipelineName,
        "properties": {
                    "activities": [
                    {
                        "name": "DatabricksNew",
                        "type": "DatabricksNotebook",
                        "linkedServiceName": {
                           "referenceName": linkedServiceName,
                            "type": "LinkedServiceReference"
                        },
                        "typeProperties": {"notebookPath": notebookPath},
                    },
                    {
                        "name": "DatabricksNew1",
                        "type": "DatabricksNotebook",
                        "linkedServiceName": {
                            "referenceName": linkedServiceName,
                            "type": "LinkedServiceReference"
                        },
                        "dependsOn": [
                            {
                                "activity": "DatabricksNew",
                                "dependencyConditions": [
                                    "Succeeded"
                                ]
                            }],
                        "typeProperties": {"notebookPath": "/pramodtestmodel.py"}
                    }

            ]
        }
    }
    response = requests.put(url, data=json.dumps(body), headers=headers)
    print(response.status_code)
    print(response.json())


def RunPipelines(subscriptionId,resourceGroupName,dataFactoryName,pipelineName,headers):
    url = "https://management.azure.com/subscriptions/" + subscriptionId + "/resourceGroups/" + resourceGroupName + "/providers/Microsoft.DataFactory/factories/" + dataFactoryName + "/pipelines/" + pipelineName + "/createRun?api-version=2018-06-01"
    body = {
    }
    response = requests.post(url, data=json.dumps(body), headers=headers)
    print(response.status_code)
    return  response.json()







tenant = '524b0e96-35a3-46ef-ade3-a76c1936a890'
authority_url = 'https://login.microsoftonline.com/' + tenant
client_id = '1ce10b53-68c2-4c25-a7a9-53c080646640'
client_secret = 'A+D6/BOcNKOA9EKhc1N7*_HEa.V[Bf0a'
resource = 'https://management.azure.com/'
subscriptionId = 'caf27308-6116-4a82-82e3-01dd49f374db'
params = {'api-version': '2019-05-10'}
resourceGroupName = 'pramodtwitterdemowk'
workspaceName = 'pramodtwitterdatabricks'
dataFactoryName ='twitterdatafactory'
apiVersion ='2019-05-10'
domain = 'centralus.azuredatabricks.net'
databrickaccessToken = 'dapi1c1c37da1da2b160e0f12d7092edafba'
databricktoken = b'dapi1c1c37da1da2b160e0f12d7092edafba'
testsourcefilePath ='/home/admininistrator/PycharmProjects/PythonProject/Week7RestApi/Testmodel.py'
trainmodelfilePath ='/home/admininistrator/PycharmProjects/PythonProject/Week7RestApi/Trainmodel.py'
tarindestinationpath = "/pramodTrainmodel.py"
testdestinationpath = "/pramodtestmodel.py"
clusterName ="Newcluster"
numWorkers = 2
dataFactoryName ="pramodDataFactory"
linkedServiceName = "pramoddatabrickslink"
pipelineName = "pramodpipeline3"


if __name__ == '__main__':

    #result = GetAccessToken(tenant,client_id,client_secret)
    context = adal.AuthenticationContext(authority_url)
    result = context.acquire_token_with_client_credentials(resource, client_id, client_secret)
    token = 'Bearer '+result['accessToken']
    headers = {'Authorization': token, 'Content-Type': 'application/json'}

    #result = CreateResourceGroups(subscriptionId,resourceGroupName,apiVersion,headers)

    #result = CreateDatabricksWorkspace(subscriptionId,resourceGroupName,workspaceName,'2018-04-01',headers)
    #print(result)

    #result = CreateDatabricksToken(domain,token,headers)
    #print(result)

    #clusterid = CreateClustar(domain,databricktoken,clusterName,numWorkers)
    #print(clusterid)

    #result = ImportNotebook(domain,databricktoken,testsourcefilePath,testdestinationpath)
    #print(result)
    #result = ImportNotebook(domain,databricktoken,trainmodelfilePath,tarindestinationpath)
    #print(result)

    clusterid ="0821-071522-augur860"
    #package ={"pickle","re","pandas","azure","sklearn.linear_model","sklearn.feature_extraction.text"}
    #result = Addlibraries(domain,databricktoken,clusterid)
    #print(result)

    #result = CreateStorageaccount(subscriptionId,resourceGroupName,"pramodsa18",headers,"2018-02-01")
    #print(result)
    #result = CreateDataFactory(subscriptionId,resourceGroupName,dataFactoryName,headers,"2018-06-01")
    #print(result)
    #result = CreatedabriksLinkedServices(subscriptionId,resourceGroupName,dataFactoryName,linkedServiceName,databrickaccessToken,domain,clusterid,headers)
    #print(result)
    result = CreatePipelines(subscriptionId,resourceGroupName,dataFactoryName,pipelineName,linkedServiceName,tarindestinationpath,headers)
    print(result)
    result = RunPipelines(subscriptionId, resourceGroupName, dataFactoryName, pipelineName, headers)
    runId = result["runId"]
    print(runId)
    url = "https://management.azure.com/subscriptions/" + subscriptionId + "/resourceGroups/" + resourceGroupName + "/providers/Microsoft.DataFactory/factories/" + dataFactoryName + "/pipelineruns/"+runId+"?api-version=2018-06-01"
    while (True):
        response = requests.get(url, headers=headers, params=params)

    print(response.status_code)

#Monitor pipeline
'''
if (response.status_code==200):
time.sleep(2)
else :
print(response.json())
'''


































































































































































































































































































































































































