
doc = '''
#%RAML 1.0
baseUri: https://anypoint.mulesoft.com/mocking/api/v1/links/7e3caca1-4721-4217-81ef-d451e1977475/ # 
title: API_RAML
version: 1.0

types:
  Auth:
    type: object
    discriminator: token
    properties:
      token : string

  Agent:
    type: object
    discriminator: enviroment, address
    properties:
      environment: string
      address: string
    example:
      agent_id: 1
      name: linux-server
      status: True
      environment: production
      address: 10.0.34.15

  Event:
    type: object
    properties:
      agent_id: string
      payload: string
      shelved: string
      
  Group:
    type: object
    discriminator: name
    properties:
      name: string
    example:
      group_id: 1
      name: admin

      
  User:
    type: object
    discriminator: user_id, name, email, group_id
    properties:
      user_id: string
      name: string
      email: string
      group_id: string
      
traits:
  dataValidation:
    responses:
      400:
        description:

/auth/token:
  description: Authentication with token

  post:
    description: Add new auth
    is: [dataValidation]
    responses:
      200:
        body:
          application/json:
            example:
              {
                Success post (/auth/token)
              }
      201:
        body:
          application/json:
            example:
              {
                Created (/auth/token)
              }
      400:
        body:
          application/json:
            example:
              {
                Bad request (/auth/token)
              }
    
/agents:
  post:
    description: Add new agent
    is: [dataValidation]
    securedBy: JWT
    body:
      {}
    responses:
      200:
        body:
          application/json:
            example:
              {
                Success post (/agents)
              }

  get:
    description: Get agents
    responses:
      200:
        body:
          application/json:
            example:
              {
                Success get (/agents)
              }  

  /{id}:
    uriParameters:
      id:
        description: Agent identifier
      
    get:
      description: Get agents/{id}
      securedBy: JWT
      responses:
        200:
          body:
            application/json:
              example:
                {
                  Success get (/agents/id)
                }
        401:
          body:
            application/json:
              example:
                {
                  Unauthorized
                }
        404:
          body:
            application/json:
              example:
                {
                  Not found
                }

    put:
      description: Updated agents/{id}
      is: [dataValidation]
      securedBy: JWT
      responses:
        200:
          body:
            application/json:
              example:
                {
                  Success put (/agents/id)
                }
        401:
          body:
            application/json:
              example:
                {
                  Unauthorized
                }
        404:
          body:
            application/json:
              example:
                {
                  Not found
                }
                
    delete:
      description: Deleted agents/{id}
      responses:
        204:
          body:
            application/json:
              example:
                {
                  Success delete (/agents/id)
                }
        404:
          body:
            application/json:
              example:
                {
                  Not found
                }        
      
  /{id}/events:
    post:
      description: Add new agents/{id}/events
      securedBy: JWT
      responses: 

    get:
      description: Get agents/{id}/events
      securedBy: JWT
      body: {}
      responses:
        200:
          body:
            application/json:
              example:
                {
                  Success get (agents/id/events)
                }
        401:
          body:
            application/json:
              example:
                {
                  Unauthorized
                }
        404:
          body:
            application/json:
              example:
                {
                  Not found
                }  

    put:
      description: Updated agents/{id}/events
      securedBy: JWT
      body:
        200:
          body:
            application/json:
              example:
                {
                  Success get (agents/id/events)
                }
        401:
          body:
            application/json:
              example:
                {
                  Unauthorized
                }
        404:
          body:
            application/json:
              example:
                {
                  Not found
                }   

    delete:
      description: Deleted agents/{id}/events
      securedBy: JWT
      body:
        application/json:
        200:
          body:
            application/json:
              example:
                {
                  Success get (agents/id/events)
                }
        401:
          body:
            application/json:
              example:
                {
                  Unauthorized
                }

/users:
  post:
    description: Post users
    body:
      application/json:
        properties: {}
    responses:
      201:
        body:
          application/json:
            example:
              {
                Created (/users)
              }
      401:
        body:
          application/json:
            example:
              {
                Unauthorized
              }
              
  get:
    description: Get users
    securedBy: JWT
    responses:
      200:
        body:
          application/json:
            example:
              {
                Success get (/users)
              }  

  /{id}:
    get:
      description: Get users/{id}
      securedBy: JWT
      responses:
        200:
          body:
            application/json:
              example:
                {
                  Success get (/users/id)
                }
        401:
          body:
            application/json:
              example:
                {
                  Unauthorized
                }
        404:
          body:
            application/json:
              example:
                {
                  Not found
                }

    put:
      description: Updated /users/{id}
      securedBy: JWT
      responses: 
        200:
          body:
            application/json:
              example:
                {
                  Success put (/users/id)
                }
        401:
          body:
            application/json:
              example:
                {
                  Unauthorized
                }
        404:      
          body:
            application/json:
              example:
                {
                  Not found
                }

    delete:
      description: Deleted /users/{id}
      securedBy: JWT
      responses:
        200:
          body:
            application/json:
              example:
                {
                  Success delete (/users/id)
                }
        401:
          body:
            application/json:
              example:
                {
                  Unauthorized
                }
        404:      
          body:
            application/json:
              example:
                {
                  Not found
                }

/groups:
  post:
    description: Post groups
    securedBy: JWT
    body:
      application/json:
        properties: {}
        example: {}
    responses:
      201:
        body:
          application/json:
            example:
              {
                Created (/groups)
              }
      401:
        body:
          application/json:
            example:
              {
                Unauthorized
              }
    
  get:
    description: Get groups
    securedBy: JWT
    responses:
      200:
        body:
          application/json:
            example:
              {
                Success get (/groups)
              }
      401:
        body:
          application/json:
            example:
              {
                Unauthorized
              }
    
  /{id}:
    get:
      description: Get groups/{id}
      securedBy: JWT
      responses:
        200:
          body:
            application/json:
              example:
                {
                  Success get (/groups/id)
                }
        401:
          body:
            application/json:
              example:
                {
                  Unauthorized
                }
        404:
          body:
            application/json:
              example:
                {
                  Not found
                }

    put:
      description: Updated groups/{id}
      securedBy: JWT
      responses: 
        200:
          body:
            application/json:
              example:
                {
                  Success put (/groups/id)
                }
        401:
          body:
            application/json:
              example:
                {
                  Unauthorized
                }

    delete:
      description: Deleted groups/{id}
      securedBy: JWT
      responses:
        200:
          body:
            application/json:
              example:
                {
                  Success delete (/groups/id)
                }

securitySchemes:
  JWT:
    type: Basic Authentication
    description: JWT Token
    settings:
      roles: []

'''
