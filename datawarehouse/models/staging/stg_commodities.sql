WITH source AS (
    SELECT
        "Date",
        "Close",
        simbolo
    FROM {{ source('dsales', 'commodities') }}
),

renamed AS (
    SELECT
        CAST("Date" AS date) AS data,
        "Close" AS valor_fechamento,
        simbolo        
    FROM source
)

SELECT *
FROM renamed
