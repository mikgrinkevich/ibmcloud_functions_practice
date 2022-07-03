# commands for deploying action

1)ibmcloud resource groups

2)ibmcloud target -g [name of resource group]
(cannot create or set resource group with free account)

3)ibmcloud fn property set --namespace 3d6c22fc-102d-4b35-959e-144e93703876

4)ibmcloud fn action create test_cli --docker paffy/belarusbank_rate_api:latest
