# thonto
A python package which can be used to convert a Python function
to JavaScript. This package is specifically designed for the MongoDB
[aggregation framework](https://docs.mongodb.com/manual/aggregation/).
It allows a Pyton developer to write 
[$function](https://docs.mongodb.com/manual/reference/operator/aggregation/function/) operators 
using Python and then convert them to JavaScript which is what the
`$function` operator expects. 

This package depends on [transcrypt](https://www.transcrypt.org/) to
do the actual conversion. 

The name is derived from the phrase py**thonto**js.
