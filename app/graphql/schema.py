from ariadne import QueryType, make_executable_schema
from app.graphql.resolver import resolve_get_order_by_id

type_defs = """
    type User {
        email: String!
    }

    type ProductLine {
        product_id: String!
        name: String!
        price_unit: Float!
        quantity: Int!
        line: String!
        subtotal: Float!
    }

    type Total {
        amount: Float!
        currency: String!
        label: String!
    }

    type Order {
        id: ID!
        user: User!
        products: [ProductLine!]!
        total: Total!
        status: String!
    }

    type Query {
        getOrderById(id: ID!): Order
    }
"""

query = QueryType()
query.set_field("getOrderById", resolve_get_order_by_id)
schema = make_executable_schema(type_defs, [query])
