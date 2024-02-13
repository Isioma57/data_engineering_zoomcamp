## Module 1 Homework

This repository contains solutions to homework questions, which require prior knowledge in Docker, SQL, and Terraform. I have set up the environment and gained practical experience with Docker and SQL as prerequisites for this assignment.

## Question 1. Knowing docker tags

Which tag has the following text? - *Automatically remove the container when it exits* 

- `--delete`
- `--rc`
- `--rmc`
- `--rm` ✅

## Question 2. Understanding docker first run 

Run docker with the python:3.9 image in an interactive mode and the entrypoint of bash.
Now check the python modules that are installed ( use ```pip list``` ). 

What is version of the package *wheel* ?

- 0.42.0 ✅
- 1.0.0
- 23.0.1
- 58.1.0

### Answer
- To run the container:
```bash
docker run -it --entrypoint=bash python:3.9
```
- To check the python modules for the version of the package wheel:
```bash
pip list | grep wheel
```

## Question 3. Count records 

How many taxi trips were totally made on September 18th 2019?

Tip: started and finished on 2019-09-18. 

Remember that `lpep_pickup_datetime` and `lpep_dropoff_datetime` columns are in the format timestamp (date and hour+min+sec) and not in date.

- 15767
- 15612 ✅
- 15859
- 89009

### Solution
```sql
SELECT 
    COUNT(*) AS count_of trips
FROM 
    green_taxi_data
WHERE 
    lpep_pickup_datetime::DATE = '2019-09-18' AND lpep_dropoff_datetime::DATE = '2019-09-18';
```

| count_of_trips | 
| -------------  | 
| 15612          |

## Question 4. Largest trip for each day

Which was the pick up day with the largest trip distance
Use the pick up time for your calculations.

- 2019-09-18
- 2019-09-16
- 2019-09-26 ✅
- 2019-09-21

### Solution
```sql
SELECT
    lpep_pickup_datetime,
    MAX(trip_distance) AS max_trip
FROM
    green_taxi_data
GROUP BY
    lpep_pickup_datetime
ORDER BY
    max_trip DESC
LIMIT 1;
```

| lpep_pickup_datetime | max_trip |
|----------------------|----------|
| 2019-09-26 19:32:52  | 341.64   |


## Question 5. Three biggest pick up Boroughs

Consider lpep_pickup_datetime in '2019-09-18' and ignoring Borough has Unknown

Which were the 3 pick up Boroughs that had a sum of total_amount superior to 50000?
 
- "Brooklyn" "Manhattan" "Queens" ✅
- "Bronx" "Brooklyn" "Manhattan"
- "Bronx" "Manhattan" "Queens" 
- "Brooklyn" "Queens" "Staten Island"

### Solution
```sql
SELECT
    "Borough",
    SUM(total_amount) AS total_amount_sum
FROM
    green_taxi_data AS gt
LEFT JOIN
    taxi_zone_data AS tz
ON
    gt."PULocationID" = tz."LocationID"
WHERE
    lpep_pickup_datetime::DATE = '2019-09-18'
    AND "Borough" != 'Unknown'
GROUP BY
    "Borough"
HAVING
    SUM(total_amount) > 50000
ORDER BY
    total_amount_sum DESC
LIMIT 3;
```

| Borough   | total_amount_sum  |
|-----------|-------------------|
| Brooklyn  | 96333.23999999906 |
| Manhattan | 92271.29999999836 |
| Queens    | 78671.70999999884 |

## Question 6. Largest tip

For the passengers picked up in September 2019 in the zone name Astoria which was the drop off zone that had the largest tip?
We want the name of the zone, not the id.

Note: it's not a typo, it's `tip` , not `trip`

- Central Park
- Jamaica
- JFK Airport ✅
- Long Island City/Queens Plaza

### Solution
```sql
SELECT
    tz_dropoff."Zone" AS dropoff_zone_name,
    MAX(gt.tip_amount) AS max_tip_amount
FROM
    green_taxi_data gt
JOIN
    taxi_zone_data tz_pickup ON gt."PULocationID" = tz_pickup."LocationID"
JOIN
    taxi_zone_data tz_dropoff ON gt."DOLocationID" = tz_dropoff."LocationID"
WHERE
    tz_pickup."Zone" = 'Astoria'
    AND EXTRACT(MONTH FROM gt.lpep_pickup_datetime) = 9
    AND EXTRACT(YEAR FROM gt.lpep_pickup_datetime) = 2019

GROUP BY
    tz_dropoff."Zone"
ORDER BY
    max_tip_amount DESC
LIMIT 1;
```

| dropoff_zone_name | max_tip_amount |
|-------------------|----------------|
| JFK Airport       | 62.31          |


## Question 7. Creating Resources
In this section homework we'll prepare the environment by creating resources in GCP with Terraform. Modify the files as necessary to create a GCP Bucket and Big Query Dataset.
After updating the main.tf and variable.tf files run:

```
terraform apply
```

Paste the output of this command into the homework submission form.
### Output
```bash
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following       
symbols:
  + create

Terraform will perform the following actions:

  # google_bigquery_dataset.demo_dataset will be created
  + resource "google_bigquery_dataset" "demo_dataset" {
      + creation_time              = (known after apply)
      + dataset_id                 = "demo_dataset"
      + default_collation          = (known after apply)
      + delete_contents_on_destroy = false
      + effective_labels           = (known after apply)
      + etag                       = (known after apply)
      + id                         = (known after apply)
      + is_case_insensitive        = (known after apply)
      + last_modified_time         = (known after apply)
      + location                   = "US"
      + max_time_travel_hours      = (known after apply)
      + project                    = "dtc-de-course-412000"
      + self_link                  = (known after apply)
      + storage_billing_model      = (known after apply)
      + terraform_labels           = (known after apply)
    }

  # google_storage_bucket.demo_buckets will be created
  + resource "google_storage_bucket" "demo_buckets" {
      + effective_labels            = (known after apply)
      + force_destroy               = true
      + id                          = (known after apply)
      + location                    = "US"
      + name                        = "dtc-de-course-412000-terra-bucket"
      + project                     = (known after apply)
      + public_access_prevention    = (known after apply)
      + rpo                         = (known after apply)
      + self_link                   = (known after apply)
      + storage_class               = "STANDARD"
      + terraform_labels            = (known after apply)
      + uniform_bucket_level_access = (known after apply)
      + url                         = (known after apply)

      + lifecycle_rule {
          + action {
              + type = "AbortIncompleteMultipartUpload"
            }
          + condition {
              + age                   = 1
              + matches_prefix        = []
              + matches_storage_class = []
              + matches_suffix        = []
              + with_state            = (known after apply)
            }
        }
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

google_bigquery_dataset.demo_dataset: Creating...
google_storage_bucket.demo_buckets: Creating...
google_bigquery_dataset.demo_dataset: Creation complete after 3s [id=projects/dtc-de-course-412000/datasets/demo_dataset]
google_storage_bucket.demo_buckets: Creation complete after 3s [id=dtc-de-course-412000-terra-bucket]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
```
