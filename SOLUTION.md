# AVIV technical test solution (by Valeria Dolce)

## Notes

My implemetation requires a new table called `price_history` where the application can store the price history. It has 4 columns:

- `id`: unique identifier
- `listing_id`: the id of the associated listing
- `price`: the amount
- `created_at`: timestamp when the new price is added

When a new listing is added, the price is automatically stored in the price_history table.
When a listing is updated, a new row is added to the `price_history` table only if the listing price has changed.

This solution doesn't require any change to the `listing` table and it has the least impact of the already implemented listings APIs.
The column `price` from the `listing` table contains the current listing price, which matches the latest price row from the `price_history` table.

No changes are required also to run all the tests.

## Questions

This section contains additional questions your expected to answer before the debrief interview.

- **What is missing with your implementation to go to production?**
  I would add more tests to increase the coverage. I would add a more better error handling system.
  In order to deploy the flask application, a cloudformation or terraform file is needed to deploy

- **How would you deploy your implementation?**
  The dockerized image can be sent to AWS ECR. Then, the webserver can be easily deployed on AWS using EC2 or other servless services such as ECS or EKS or Fargate etc based on the budget, requirements and potential traffic. It requires a AWS API Gateway.
  The DB can be deployed on AWS RDS or Aurora serverless.

- **If you had to implement the same application from scratch, what would you do differently?**

  I would have use FastAPI which has best performaces, native async support, built-in pydantic validation, automatic APIs documentation.

- **The application aims at storing hundreds of thousands listings and millions of prices, and be accessed by millions
  of users every month. What should be anticipated and done to handle it?**

  To improve the query performances, an index can be created on the `price_history(listing_id)`, based on the current queries and APIs (but potentially also on created_date column).
  Adding a in-memory DB (e.g. Redis) as caching layer for frequently accessed price data can help.

  To improve the scalability, we need to have multiple RDS replicas and an autoscaling policy in place for service used to host the webserver.

  NB: You must update the [given architecture schema](./schemas/Aviv_Technical_Test_Architecture.drawio) by importing it
  on [diagrams.net](https://app.diagrams.net/)

  Based on my changes no need to update the architecture schema.
