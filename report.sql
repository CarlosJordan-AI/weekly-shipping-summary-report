-- Report: Weekly shipping cost summary by Partner + Carrier (+ Factory)
-- Filters: :start (YYYY-MM-DD), optional :factory, :partner, :carrier
-- Only includes invoiced shipping.

SELECT
  o.InvoiceWeek,
  o.CustomPartnerId,
  o.ShippingCarrier,
  o.FactoryId,
  COUNT(DISTINCT o.id)              AS Orders,
  COUNT(sp.id)                      AS Packages,
  SUM(o.ShippingBase)               AS ShippingBase,
  SUM(o.ShippingAmount)             AS ShippingAmount
FROM "order" o
JOIN "shippackage" sp ON sp.orderid = o.id
WHERE
  o.IsShippingInvoiced = 1
  AND o.IsInvoiced = 1
  AND o.SortedOnUtc >= :start
  AND (:factory IS NULL OR o.FactoryId = :factory)
  AND (:partner = ''  OR o.CustomPartnerId = :partner)
  AND (:carrier = ''  OR o.ShippingCarrier = :carrier)
GROUP BY
  o.InvoiceWeek,
  o.CustomPartnerId,
  o.ShippingCarrier,
  o.FactoryId
ORDER BY
  o.InvoiceWeek ASC,
  o.CustomPartnerId ASC,
  o.ShippingCarrier ASC,
  o.FactoryId ASC;
