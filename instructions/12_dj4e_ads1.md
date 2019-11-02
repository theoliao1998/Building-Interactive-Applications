<!DOCTYPE html>
    <html>
      <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>DJ4E - Django for Everybody</title>
        <script>
        var _TSUGI = {
            context_title: "SI 664 001 FA 2019",
            link_title: "Tool: Autograder: Request-Response Cycle",
            user_displayname: "Xinhao Liao",
            user_locale: "en",
            ajax_session: false,
            heartbeat: 1500000,
            heartbeat_url: "https://www.dj4e.com/tsugi/util/heartbeat?msec=1500000",
            rest_path: {"parent":"\/assn","base_url":"https:\/\/www.dj4e.com","controller":"dj4e_ads1.md","extra":"","action":false,"parameters":[],"current":"\/assn\/dj4e_ads1.md","full":"\/assn\/dj4e_ads1.md"},
            spinnerUrl: "https://static.tsugi.org/img/spinner.gif",
            staticroot: "https://static.tsugi.org",
            websocket_url: false,
            websocket_token: false,
            window_close_message: "Application complete",
            session_expire_message: "Your session has expired"
        }
        </script>
        <!-- Tiny bit of JS -->
        <script src="https://static.tsugi.org/js/tsugiscripts_head.js"></script>
        <!-- Le styles -->
        <link href="https://static.tsugi.org/bootstrap-3.4.1/css/bootstrap.min.css" rel="stylesheet">
        <link href="https://static.tsugi.org/js/jquery-ui-1.11.4/jquery-ui.min.css" rel="stylesheet">
                <link href="https://static.tsugi.org/fontawesome-free-5.8.2-web/css/all.css" rel="stylesheet">
        <link href="https://static.tsugi.org/fontawesome-free-5.8.2-web/css/v4-shims.css" rel="stylesheet">
        <style>:root {--primary:#0D47A1;--primary-border:#0d4295;--primary-darker:#0c4091;--primary-darkest:#0b3b85;--secondary:#EEEEEE;--text:#111111;--text-light:#5E5E5E;--font-family:sans-serif;--font-size:14px;}</style>
          <link href="https://static.tsugi.org/css/tsugi.css" rel="stylesheet">

          <style>
                        </style>
<style>
a[target="_blank"]:after {
    font-family: 'Font Awesome 5 Free';
    font-weight: 600;
    content: " \f35d";
}
.goog-te-banner-frame.skiptranslate {
    display: none !important;
    }
body {
    top: 0px !important;
    }
</style>

        <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
        <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
        <!--[if lt IE 9]>
          <script src="https://www.dj4e.com/tsugi/vendor/tsugi/lib/static/js/html5shiv/html5shiv.js"></script>
          <script src="https://www.dj4e.com/tsugi/vendor/tsugi/lib/static/js/respond/respond.min.js"></script>
        <![endif]-->

    <script type="text/javascript">CSRF_TOKEN = "5dbde64861f20";</script>
</head>
<body prefix="oer: http://oerschema.org">
<div id="body_container">
<script>
if (window!=window.top) {
    document.getElementById("body_container").className = "container-fluid";
} else {
    document.getElementById("body_container").className = "container";
}
</script>
<nav class="navbar navbar-inverse navbar-fixed-top" role="navigation" id="tsugi_main_nav_bar" style="display:none">  <div class="container-fluid">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="https://www.dj4e.com">DJ4E</a>
    </div>
    <div class="navbar-collapse collapse">
      <ul class="nav navbar-nav navbar-main">
        <li><a href="https://www.dj4e.com/lessons" >Lessons</a></li>
        <li><a href="https://www.dj4e.com/assn" >Assignments</a></li>
      </ul>
      <ul class="nav navbar-nav navbar-right">
        <li><a href="http://www.dr-chuck.com" target="_blank" >Instructor</a></li>
        <li><a href="https://www.dj4e.com/tsugi/login.php" >Login</a></li>
      </ul>
    </div> <!--/.nav-collapse -->
  </div> <!--container -->
</nav>
<script>
if ( ! inIframe() ) {
  document.getElementById('tsugi_main_nav_bar').style.display = 'block';
  document.getElementsByTagName('body')[0].style.paddingTop = '5.93rem';
}
</script>
<div id="flashmessages"></div><style>
center {
    padding-bottom: 10px;
}
@media print {
    #chapters {
        display: none;
    }
}
a[target="_blank"]:after {
  content: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAQElEQVR42qXKwQkAIAxDUUdxtO6/RBQkQZvSi8I/pL4BoGw/XPkh4XigPmsUgh0626AjRsgxHTkUThsG2T/sIlzdTsp52kSS1wAAAABJRU5ErkJggg==);
  margin: 0 3px 0 5px;
}
</style>
</head>
<body prefix="oer: http://oerschema.org">
<div id="body_container">
<script>
if (window!=window.top) {
    document.getElementById("body_container").className = "container-fluid";
} else {
    document.getElementById("body_container").className = "container";
}
</script>
<script>
function onSelect() {
    console.log($('#chapters').val());
    window.location = $('#chapters').val();
}
</script>
<div style="float:right">
<select id="chapters" onchange="onSelect();">
  <option value="paw_install.md">Django and PythonAnywhere</option>
  <option value="paw_skeleton.md">Skeleton web site</option>
  <option value="paw_models.md">Django Models</option>
  <option value="paw_admin.md">Django Admin</option>
  <option value="dj4e_load.md">Batch Loading Data</option>
  <option value="paw_home.md">Django Home Page</option>
  <option value="paw_details.md">Django Detail Pages</option>
  <option value="paw_sessions.md">Django Sessions</option>
  <option value="paw_users.md">Django Users</option>
  <option value="paw_forms.md">Django Forms</option>
  <option value="paw_github.md">Using GitHub</option>
  <option value="dj_install.md">Installing Django Locally</option>
  <option value="dj4e_hello.md">Hello World</option>
  <option value="dj4e_autos.md">Autos CRUD</option>
  <option value="dj4e_ads1.md" selected>AdList Milestone #1</option>
  <option value="dj4e_ads2.md">AdList Milestone #2</option>
  <option value="dj4e_ads3.md">AdList Milestone #3</option>
  <option value="dj4e_ads4.md">AdList Milestone #4</option>
</select>
</div>
<h1>Building a Classified Ad Web Site</h1>
<p>In this assignment, you will build a web site that is roughly equivalent to</p>
<p><a href="https://chucklist.dj4e.com/m1">https://chucklist.dj4e.com/m1</a></p>
<p>This web site is a classified ad web site.   People can view ads without logging in
and if they log in, they can create their own ads.   It uses a social login
that allows loging using github accounts.</p>
<p>You will build this application by borrowing parts and pieces from the code that runs</p>
<p><a href="https://samples.dj4e.com/">https://samples.dj4e.com/</a></p>
<p>and combining them into a single application.</p>
<p>Make sure to get the latest version of dj4e-samples.  If you have never checked it out
on PythonAnywhere:</p>
<pre><code>cd ~
git clone https://github.com/csev/dj4e-samples</code></pre>
<p>If it already is on PythonAnywhere:</p>
<pre><code>cd ~/dj4e-samples
git pull</code></pre>
<p>Note: Do <strong>not</strong> build this application by forking the sample application repository
and hacking it.  There is just too much cruft in that repository that will make it hard to develop
your application.   You will end up with a lot cleaner code by taking pieces from
the sample applications and copying them into a new application.   At some point,
we will ask you to hand
in the source of your application and we will check to make sure you are not using a fork
of the sample application.</p>
<h2>Borrowing from the Samples Repository</h2>
<p>(1) Make a new project under your <code>django_projects</code> called <code>adlist</code>.</p>
<p>(2) Copy <code>dj4e-samples/requirements.txt</code> to <code>django_projects/adlist/requirements.txt</code> and launch a shell.  If you are using
virtual environments you must run the <code>pip</code> command in your virtual environment.   In PythonAnywhere
under Linux you would say:</p>
<pre><code>workon django2</code></pre>
<p>The run:</p>
<pre><code>pip install -r requirements.txt   # or pip3</code></pre>
<p>This will pull in important extra libraries that your application will need.  On PythonAnywhere
make sure to double check under the <code>Web</code> tab under the <code>Virtualenv</code> section that you have
it set to something like:</p>
<pre><code>/home/--your-account---/.virtualenvs/django2</code></pre>
<p>So that your python application is run within the virtual environment.</p>
<p>(3) Adapt <code>django_projects/adlist/adlist/settings.py</code> to pull in most of <code>dj4e-samples/dj4e-samples/settings.py</code>.</p>
<p>You might even want to copy <code>dj4e-samples/dj4e-samples/settings.py</code> to
<code>dango_projects/adlist/adlist/settings.py</code> and then delete
all the <code>INSTALLED_APPLICATIONS</code> after <code>home</code> and add <code>ads</code>.  You also have to search
and replace <code>dj4e-samples</code> with <code>adlist</code> in a few places.</p>
<p>Alternatively, you can look through the <code>dj4e-samples/dj4e-samples/settings.py</code> and copy pertinent lines
into <code>django_project/adlist/adlist/settings.py</code> - some lines have an &quot;Add&quot; comment to help draw your attention
to things to copy across.</p>
<p>In addition to all the other settings fixes, make sure to add a line
to <code>django_project/adlist/adlist/settings.py</code> like this:</p>
<pre><code># Used for a default title
APP_NAME = 'ChucksList'</code></pre>
<p>This shows up in default page titles and default page navigation.</p>
<p>(4) Copy the entire <code>home</code> application folder from into your adlist project.  This should not
need much changing - it has things like base templates, and login templates and is designed
to quickly get up to speed getting started in a new project.  </p>
<pre><code>mkdir ~/django_projects/adlist/home
cp -r ~/dj4e-samples/dj4e-samples/home/* ~/django_projects/adlist/home</code></pre>
<p>(5) Edit your <code>adlist/urls.py</code> and pull in some of the paths from <code>dj4e-samples/dj4e-samples/urls.py</code>.   Look
for lines that say &quot;Keep&quot; to help make sure you configure all of the optional features.</p>
<p>At this point, you should be able to run:</p>
<pre><code>python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser</code></pre>
<p>There won't be many working urls.  Try these two to see if you have the home code
working properly:</p>
<pre><code>https://your-account.pythonanywhere.com/accounts/login
https://your-account.pythonanywhere.com/favicon.ico</code></pre>
<p>Don't worry about social login yet.  We will get to that later.
Favicons are shown in the tabs in the browser.  We will get to favicons later too :)</p>
<p>If you get an error like <code>Could not import github_settings.py for social_django</code>
when running <code>manage.py</code> or restarting your PythonAnywhere webapp,
don't worry - you will see this warning until you set up social login.</p>
<h2>Building the Ads Application</h2>
<p>In this section, you will pull bits and pieces of the sample applications repository and pull them
into your <code>ads</code> application.</p>
<p>(1) Create a new <code>ads</code> application within your <code>adlist</code> project.</p>
<p>(2) Use this in your <code>ads/model.py</code>:</p>
<pre><code>from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.conf import settings

class Ad(models.Model) :
    title = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Title must be greater than 2 characters")]
    )
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    text = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in the admin list
    def __str__(self):
        return self.title</code></pre>
<p>(3) Pull in pieces of <code>myarts</code> application other than <code>models.py</code>.  Then adapt the
<code>admin.py</code>, <code>views.py</code>, <code>urls.py</code>, and templates to be suitable for a classified
ad application and the above model.   A big part of this assignment is to use the
view classes that are in <code>owner.py</code> and used in <code>views.py</code>.  The new <code>owner</code> field should
not be shown to the user on the create and update forms, it should be automatically set
by the classes like <code>OwnerCreateView</code> in <code>owner.py</code>.  If you see an &quot;owner&quot; drop down
in your user interface the program is not implemented correctly and will fail the autograder.</p>
<p>(4) When you are implementing the update and delete views, make sure to follow the url patterns
the update and delete operations.  They should be of the form <code>/ad/14/update</code>
and <code>/ad/14/delete</code>.  Something like the following should work in your <code>urls.py</code>:</p>
<pre><code>urlpatterns = [
    path('', views.AdListView.as_view()),
    path('ads', views.AdListView.as_view(), name='ads'),
    path('ad/&lt;int:pk&gt;', views.AdDetailView.as_view(), name='ad_detail'),
    path('ad/create',
        views.AdCreateView.as_view(success_url=reverse_lazy('ads')), name='ad_create'),
    path('ad/&lt;int:pk&gt;/update',
        views.AdUpdateView.as_view(success_url=reverse_lazy('ads')), name='ad_update'),
    path('ad/&lt;int:pk&gt;/delete',
        views.AdDeleteView.as_view(success_url=reverse_lazy('ads')), name='ad_delete'),
]</code></pre>
<p>(5) Change your <code>adlist/urls.py</code> to use the following url patterns so the main route ('')
goes to the <code>ads</code> application.</p>
<pre><code>urlpatterns = [
    path('', include('ads.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
]</code></pre>
<h2>Adding the Bootstrap menu to the top of the page</h2>
<p>Next we will add the bootstrap navigation bar to the top of your application as shown in:</p>
<p><a href="https://chucklist.dj4e.com/">https://chucklist.dj4e.com/</a></p>
<p>This top bar includes a 'Create Ad' navigation item and the login/logout navigation as well as
the gravatar when the user logs in.</p>
<p>(1) Copy <code>base_menu.html</code> template from <code>dj4e-samples/menu</code> application and into <code>ads/templates/ads</code>.  This should
extend <code>base_bootstrap.html</code> (in your <code>home</code> application).  You will need to adjust the navigation and url
lookups in this file to match the naviation in the sample implementation.</p>
<p>(2) Then edit all four of the <code>ads_</code> files in <code>ads/templates/ads</code> to change them so
they extend <code>ads/base_menu.html</code>.  Change the first line of each file from:</p>
<pre><code>{% extends "base_bootstrap.html" %}</code></pre>
<p>to be.</p>
<pre><code>{% extends "ads/base_menu.html" %}</code></pre>
<p>(3) Then edit <code>ads/templates/base_menu.html</code> replace the main lists of navigation items as follows:</p>
<pre><code>&lt;nav class="navbar navbar-default navbar-inverse"&gt;
  &lt;div class="container-fluid"&gt;
    &lt;div class="navbar-header"&gt;
        &lt;a class="navbar-brand" href="/"&gt;{{ settings.APP_NAME }}&lt;/a&gt;
    &lt;/div&gt;
    &lt;!-- https://stackoverflow.com/questions/22047251/django-dynamically-get-view-url-and-check-if-its-the-current-page --&gt;
    &lt;ul class="nav navbar-nav"&gt;
      {% url 'ads' as ads %}
      &lt;li {% if request.get_full_path == ads %}class="active"{% endif %}&gt;
          &lt;a href="{% url 'app_name_here:ads' %}"&gt;Ads&lt;/a&gt;&lt;/li&gt;
    &lt;/ul&gt;
    &lt;ul class="nav navbar-nav navbar-right"&gt;
        {% if user.is_authenticated %}
        &lt;li&gt;
        &lt;a href="{% url 'app_name_here:ad_create' %}"&gt;Create Ad&lt;/a&gt;
        &lt;/li&gt;
        &lt;li class="dropdown"&gt;
            &lt;a href="#" data-toggle="dropdown" class="dropdown-toggle"&gt;
                &lt;img style="width: 25px;" src="{{ user|gravatar:60 }}"/&gt;&lt;b class="caret"&gt;&lt;/b&gt;
            &lt;/a&gt;
            &lt;ul class="dropdown-menu"&gt;
                &lt;li&gt;&lt;a href="{% url 'logout' %}?next={% url 'app_name_here:ads' %}"&gt;Logout&lt;/a&gt;&lt;/li&gt;
            &lt;/ul&gt;
        &lt;/li&gt;
        {% else %}
        &lt;li&gt;
        &lt;a href="{% url 'login' %}?next={% url 'app_name_here:ads' %}"&gt;Login&lt;/a&gt;
        &lt;/li&gt;
        {% endif %}
    &lt;/ul&gt;
  &lt;/div&gt;
&lt;/nav&gt;</code></pre>
<p>(4) Find the line in your <code>base_bootstrap.html</code> that looks like this:</p>
<pre><code>    &lt;meta name="wa4e-code" content="99999999"&gt;</code></pre>
<p>and change the <code>9999999</code>  to be &quot;<span id="wa4e-code">missing</span>&quot;</p>
<p>Make sure to check the autograder for additional markup requirements.</p>
<p>When you are done, you should see an 'Ads' menu on the left and a 'Create Ad' link on the right just like the
sample implementation.</p>
<h2>Fun Challenges</h2>
<p>(1) Make yourself a gravatar at <a href="https://en.gravatar.com/">https://en.gravatar.com/</a> - it is super easy and you will see your
avatar when you log in in your application and elsewhere with gravatar enabled apps. The gravatar can be
any thing you like - it does not have to be a picture of you.</p>
<p>(2) Change your <code>home/static/favicon.ico</code> to a favicon of your own making.   I made my favicon
at <a href="https://favicon.io/favicon-generator/">https://favicon.io/favicon-generator/</a> - it might not change instantly after you update the favicon
because they are cached extensively.   Probably the best way to test is to go right to the favicon url
after up update the file and press 'Refresh' and.or switch browsers.</p>
<p>(3) Make social login work.  Take a look at <code>dj4e-samples/dj4e-samples/github_settings-dist.py</code>, copy it into
<code>adlist/github_settings.py</code> and go through the process on github to get your client ID and
secret.   The documentation is in comments in the <code>github_setting.py</code> file.
You can register two applications - one on localhost and one on PythonAnywhere.  If you are
using github on localhost - make sure that you
register <code>http://127.0.0.1:8000/</code> instead of <code>http://localhost:8000/</code> and use that in your browser
to test your site.  If you use localhost, you probably will get the <code>The redirect_uri MUST match the registered callback URL for this application.</code> error message when you use social login.</p>
<h2>Working with Ambiguity</h2>
<p>This assignment is more vague than previous assignments - on purpose.  The goal is to get
closer to the development model for actual applications.  You know what you want to build
and start with a mostly blank slate.  You look at sample code, reuse some code form stuff
you build earlier, do some online
searching and glue pieces of what you find together to make your application.  Of course as
you are gluing bits from various places together, they always break and you have to adjust things
so they fit in your application.</p>
<p>So this is kind of like the real world - when you have to build your own first application
for someone else.</p>
<p>Let us know if you really get stuck.  We want you to succeed in this assignment.</p>
<script>
var d= new Date();
var code = "42"+((Math.floor(d.getTime()/1234567)*123456)+42)
document.getElementById("wa4e-code").innerHTML = code;
</script><script src="https://static.tsugi.org/js/jquery-1.11.3.js"></script>
<script src="https://static.tsugi.org/bootstrap-3.4.1/js/bootstrap.min.js"></script>
<script src="https://static.tsugi.org/js/jquery-ui-1.11.4/jquery-ui.min.js"></script>
<script src="https://static.tsugi.org/js/jquery.timeago-1.6.3.js"></script>
<script src="https://static.tsugi.org/js/handlebars-v4.0.2.js"></script>
<script src="https://static.tsugi.org/tmpljs-3.8.0/tmpl.min.js"></script>
<script src="https://static.tsugi.org/js/tsugiscripts.js"></script>
<script type="text/javascript">
    HEARTBEAT_TIMEOUT = setTimeout(doHeartBeat, _TSUGI.heartbeat);
    tsugiEmbedMenu();
</script>
<div id="google_translate_element" style="position: fixed; right: 1em; bottom: 0.25em;"></div><script type="text/javascript">
function googleTranslateElementInit() {
  new google.translate.TranslateElement({pageLanguage: "en", layout: google.translate.TranslateElement.InlineLayout.SIMPLE
    }, "google_translate_element");
}
</script><script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
<script>
// PHP VERSION 7.0 and 7.1 HACK
// https://stackoverflow.com/questions/44980654/how-can-i-make-trans-sid-cookie-less-sessions-work-in-php-7-1
$('a').each(function (x) {
    var href = $(this).attr('href');
    if ( ! href ) return;
    if ( ! href.startsWith('#') ) return;
    var pos = href.indexOf('/?');
    if ( pos < 1 ) return;
    console.dir('Patching broken # href='+href);
    href = href.substring(0,pos);
    $(this).attr('href', href);
});

</script>
<script>
// https://stackoverflow.com/questions/7901679/jquery-add-target-blank-for-outgoing-link
$(window).load(function() {
    $('a[href^="http"]').attr('target', function() {
      if(this.host == location.host) return '_self'
      else return '_blank'
    });
});
</script>

</div></body>
</html>
