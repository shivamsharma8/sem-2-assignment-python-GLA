import re

pattern = r"[A-Z]+la"

text = ''' 
<title>GLAMS - GLA University</title>
    <!-- META TAGS -->
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="GLA University, Mathura">
    <meta name="keyword" content="Education, GLA University, Clubs">
    <!-- FAV ICON(BROWSER TAB ICON) -->
    <link rel="shortcut icon" href="/Static/images/fav.ico" type="image/x-icon">
    <!-- GOOGLE FONT -->
    <link rel="stylesheet" href="/Static/css/font.css">
    <!-- FONTAWESOME ICONS -->
    <link rel="stylesheet" href="/Static/css/font-awesome.min.css">
    <!-- ALL CSS FILES -->
    <link href="/Static/css/materialize.css" rel="stylesheet">
    <link href="/Static/css/bootstrap.css" rel="stylesheet" />
    <link href="/Static/css/style.css" rel="stylesheet" />
    <!-- RESPONSIVE.CSS ONLY FOR MOBILE AND TABLET VIEWS -->
    <link href="/Static/css/style-mob.css" rel="stylesheet" />
    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
    <script src="/Static/js/html5shiv.js"></script>
    <script src="/Static/js/respond.min.js"></script>
    <![endif]-->
    <script src="/assets/scripts/DemoSec.js"></script>

    <script src="/Scripts/angular.js"></script>
    <script src="/Scripts/angular-sanitize.js"></script>
    <script src="/Scripts/angular-route.js"></script>
    <script src="/Scripts/ng-pattern-restrict.min.js"></script>
    <script src="/assets/scripts/ui-bootstrap-tpls-0.10.0.js"></script>

    <script src="/Scripts/MyAngularScript/MyApp.js"></script>
    <!-- Global site tag (gtag.js) - Google Analytics -->

    <script async src="https://www.googletagmanager.com/gtag/js?id=G-C1BE720JQ4"></script>
    <script>
      window.dataLayer = window
'''

matches = re.finditer(pattern , text)
for match in matches:
    print(match)
