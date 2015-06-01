<!DOCTYPE html>
<html lang="en">
<head>
    {% block head %}
      <link rel="stylesheet" />
      <title>{% block title %}{% endblock %}</title>
      <meta charset='utf-8'>
    {% endblock %}
</head>
<body>
    <div id="content">{% block content %}{% endblock %}</div>
    
</body>
</html>