{# Load the basic template provided by Jupyter #}
{% extends 'basic.tpl' %}

{# Remove the warning output #}
{% block stream_stderr %}
{% endblock stream_stderr %}

{# Include only the cells tagged by show #}
{% block any_cell %}
{% if 'show' in cell['metadata'].get('tags', []) %}
    {{ super() }}
{% else %}
{% endif %}
{% endblock any_cell %}

{% block header %}
<!DOCTYPE html>
<html>
    <head>
      <meta charset="utf-8" />
      <script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>
      <link rel="stylesheet" type="text/css" href="style.css">
    </head>
{% endblock header %}
{% block body %}
    <body>
        {{ super() }}
    </body>
{% endblock body %}
{% block footer %}
</html>
{% endblock footer %}
