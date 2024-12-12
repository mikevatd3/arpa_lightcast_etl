# ARPA Lightcast ETL

"The scripts to pull data from the Lightcast APIs for the use in the Digital Equity Database (ARPA)."


## Target data structure

[The target lightcast datastructure has four entities: Geographies, Opportunities, Occupations, Skills. A geography has many opportunities. Those opportunities are in particular occupations. Those occupations require specific skills. Each of these has descriptions. Opportunities also has a count of the jobs of a given occupation in a geography.]((https://github.com/mikevatd3/arpa_lightcast_etl/blob/main/arpa-lightcast-dataset.png?raw=true))

