# Microsoft Azure
## Deploy an Article CMS to Azure

### App Service:
>Azure Web Apps is a fast and simple way to create web apps using ASP.NET, Java, Node.js or PHP.It has built-in CI/CD integration and has zero-downtime deployments. Its take away most of the complexity and lets us concentrate more on the application itself. With me, it is more easier than config and build it in VM. 

Approx Monthly cost:

| Service | Cost (Per Month)|
| ------ | ------ |
| App Service | $50 |
|Storage account | $10|
|SQL Database cost | $370|
#### Approximate Total $430
#### Pros:
- It has built in infrastructure maintenance, scaling.
- high availability with SLA-backed uptime of 99.95 %
- Continuous Deployment (CI / CD) workflow backed up with [AzureRepos, GitHub, BitBucket]
#### Cons:
- Provides no control over the infrastructure 

### Virtual Machines:
>Azure Virtual Machines let us provision Windows or Linux VMs in seconds, can be deployed with own VM image or images from the Azure Marketplace, ability to scale from one to thousands of VM instances in minutes with Azure Virtual Machine Scale Sets.

Approximate Monthly cost:

| Service | Cost (Per Month)|
| ------ | ------ |
| Virtual Machine | $150 |
|Storage account | $22|
|SQL Database cost | $370|
#### Approximate Total $540
#### Pros:
- It provides complete control over infrastructure.
- high availability with SLA-backed uptime of 99.5%
- can be scaled from one to thousands of VM instances.
#### Cons:
- Increased Complexity compared to App Service

## Summary
> If you one to deploy an web services faster and easier, you should choose App Services, casue it is really easy to use. In orthes case, if you want to deploy an web services with more configurable choice, you can choose an VM to do it.
> In this case, this application isn't has an critical in business or any risk, so I decide to choose App services.