{# Load the basic template provided by Jupyter #}
{% extends 'basic.tpl' %}

{# Remove the input blocks (code) #}
{% block input_group %}
{% endblock input_group %}

{# Remove the output prompt (equivalent to option --no-prompt)#}
{% block output_area_prompt %}
{% endblock output_area_prompt %}

{% block any_cell %}
{% if 'no_report' in cell['metadata'].get('tags', []) %}
{% else %}
    {{ super() }}
{% endif %}
{% endblock any_cell %}

{%- block header -%}
<!DOCTYPE html>
<html>
    <head>
      <meta charset="utf-8" />
      <script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>
      <link rel="stylesheet" type="text/css" href="style.css">
    </head>
{%- endblock header -%}
{%- block body -%}
    <body>
        {{ super() }}
    </body>
{%- endblock body -%}
{%- block footer -%}
</html>
{%- endblock footer -%}
