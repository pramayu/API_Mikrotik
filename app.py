from flask import Flask
from configure import Development
from flask_graphql import GraphQLView
from controller import schema

app = Flask(__name__)
app.config.from_object(Development)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))