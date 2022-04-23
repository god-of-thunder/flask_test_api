# 新增一筆購買單 api
## POST/order/add
### request body schema
application/json

### request format

customer_name:string
<font color=red>required</font>

customer_id:string
<font color=red>required</font>

product_name:string
<font color=red>required</font>

product_id:string
<font color=red>required</font>

amount:int
<font color=red>required</font>

price:int
<font color=red>required</font>


### request sample
{
    "customer_name":"VincentWang",
    "customer_id":"V04",
    "product_name":"perfume",
    "product_id":"075",
    "amount":1,
    "price":100
}

### response 
2xx
### response schema
application/json

### response format

msg:string
<font color=red>required</font>

### response sample
{
    "msg": "perfume transction success"
}
# 修改一筆購買單 api
## PUT/order/modify
### request body schema
application/json

### request format

product_id:string
<font color=red>required</font>

order_id:string
<font color=red>required</font>

amount:int
<font color=red>required</font>



### request sample
{
    "product_id":"075",
    "order_id":"20220423101908239727",
    "amount":3
}

### response 
2xx
### response schema
application/json

### response format

msg:string
<font color=red>required</font>

### response sample
{
    "msg": "modify amount : 3  success"
}
