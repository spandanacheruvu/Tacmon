




<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>Example-Sketch-for-IMU-including-Kalman-filter/README.md at master · TKJElectronics/Example-Sketch-for-IMU-including-Kalman-filter · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <meta property="fb:app_id" content="1401488693436528"/>

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="TKJElectronics/Example-Sketch-for-IMU-including-Kalman-filter" name="twitter:title" /><meta content="Example-Sketch-for-IMU-including-Kalman-filter - Software for &amp;quot;Guide to gyro and accelerometer with Arduino including Kalman filtering&amp;quot;" name="twitter:description" /><meta content="https://0.gravatar.com/avatar/747605b15879bd4f49756ed178dad661?d=https%3A%2F%2Fidenticons.github.com%2F70ee2f3753c812806f79fcd20768c409.png&amp;r=x&amp;s=400" name="twitter:image:src" />
<meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://0.gravatar.com/avatar/747605b15879bd4f49756ed178dad661?d=https%3A%2F%2Fidenticons.github.com%2F70ee2f3753c812806f79fcd20768c409.png&amp;r=x&amp;s=400" property="og:image" /><meta content="TKJElectronics/Example-Sketch-for-IMU-including-Kalman-filter" property="og:title" /><meta content="https://github.com/TKJElectronics/Example-Sketch-for-IMU-including-Kalman-filter" property="og:url" /><meta content="Example-Sketch-for-IMU-including-Kalman-filter - Software for &quot;Guide to gyro and accelerometer with Arduino including Kalman filtering&quot;" property="og:description" />

    <meta name="hostname" content="github-fe137-cp1-prd.iad.github.net">
    <meta name="ruby" content="ruby 2.1.0p0-github-tcmalloc (87d8860372) [x86_64-linux]">
    <link rel="assets" href="https://github.global.ssl.fastly.net/">
    <link rel="conduit-xhr" href="https://ghconduit.com:25035/">
    <link rel="xhr-socket" href="/_sockets" />
    


    <meta name="msapplication-TileImage" content="/windows-tile.png" />
    <meta name="msapplication-TileColor" content="#ffffff" />
    <meta name="selected-link" value="repo_source" data-pjax-transient />
    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="6A4DB281:0718:2E4D7EA:52F32857" name="octolytics-dimension-request_id" />
    

    
    
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />

    <meta content="authenticity_token" name="csrf-param" />
<meta content="OynS6p0l3XIqfESLk5lWIFNj+fJO45q1sKpkulPWja4=" name="csrf-token" />

    <link href="https://github.global.ssl.fastly.net/assets/github-c8eaece92b2ba4da8cdfd619fae679b5161d6b98.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://github.global.ssl.fastly.net/assets/github2-3477716079e37c0883e7d9605262f998e1cb8623.css" media="all" rel="stylesheet" type="text/css" />
    


      <script src="https://github.global.ssl.fastly.net/assets/frameworks-e8d62aa911c75d1d60662859d52c3cf1232675e6.js" type="text/javascript"></script>
      <script async="async" defer="defer" src="https://github.global.ssl.fastly.net/assets/github-14ac102c26f8173d1f299518baacccd70cada295.js" type="text/javascript"></script>
      
      <meta http-equiv="x-pjax-version" content="f3e5937f4ecb01f2fbfb5fd1e62f9536">

        <link data-pjax-transient rel='permalink' href='/TKJElectronics/Example-Sketch-for-IMU-including-Kalman-filter/blob/dd40c9b1cf5e84fae4f4e83c579bf88a04545c09/README.md'>

  <meta name="description" content="Example-Sketch-for-IMU-including-Kalman-filter - Software for &quot;Guide to gyro and accelerometer with Arduino including Kalman filtering&quot;" />

  <meta content="1304816" name="octolytics-dimension-user_id" /><meta content="TKJElectronics" name="octolytics-dimension-user_login" /><meta content="4500853" name="octolytics-dimension-repository_id" /><meta content="TKJElectronics/Example-Sketch-for-IMU-including-Kalman-filter" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="4500853" name="octolytics-dimension-repository_network_root_id" /><meta content="TKJElectronics/Example-Sketch-for-IMU-including-Kalman-filter" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/TKJElectronics/Example-Sketch-for-IMU-including-Kalman-filter/commits/master.atom" rel="alternate" title="Recent Commits to Example-Sketch-for-IMU-including-Kalman-filter:master" type="application/atom+xml" />

  </head>


  <body class="logged_out  env-production windows vis-public page-blob">
    <div class="wrapper">
      
      
      
      


      
      <div class="header header-logged-out">
  <div class="container clearfix">

    <a class="header-logo-wordmark" href="https://github.com/">
      <span class="mega-octicon octicon-logo-github"></span>
    </a>

    <div class="header-actions">
        <a class="button primary" href="/join">Sign up</a>
      <a class="button signin" href="/login?return_to=%2FTKJElectronics%2FExample-Sketch-for-IMU-including-Kalman-filter%2Fblob%2Fmaster%2FREADME.md">Sign in</a>
    </div>

    <div class="command-bar js-command-bar  in-repository">

      <ul class="top-nav">
          <li class="explore"><a href="/explore">Explore</a></li>
        <li class="features"><a href="/features">Features</a></li>
          <li class="enterprise"><a href="https://enterprise.github.com/">Enterprise</a></li>
          <li class="blog"><a href="/blog">Blog</a></li>
      </ul>
        <form accept-charset="UTF-8" action="/search" class="command-bar-form" id="top_search_form" method="get">

<input type="text" data-hotkey="/ s" name="q" id="js-command-bar-field" placeholder="Search or type a command" tabindex="1" autocapitalize="off"
    
    
      data-repo="TKJElectronics/Example-Sketch-for-IMU-including-Kalman-filter"
      data-branch="master"
      data-sha="068a6fbcf0d01b2baeb47bcf5290cc7ba1d6986d"
  >

    <input type="hidden" name="nwo" value="TKJElectronics/Example-Sketch-for-IMU-including-Kalman-filter" />

    <div class="select-menu js-menu-container js-select-menu search-context-select-menu">
      <span class="minibutton select-menu-button js-menu-target">
        <span class="js-select-button">This repository</span>
      </span>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container">
        <div class="select-menu-modal">

          <div class="select-menu-item js-navigation-item js-this-repository-navigation-item selected">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" class="js-search-this-repository" name="search_target" value="repository" checked="checked" />
            <div class="select-menu-item-text js-select-button-text">This repository</div>
          </div> <!-- /.select-menu-item -->

          <div class="select-menu-item js-navigation-item js-all-repositories-navigation-item">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" name="search_target" value="global" />
            <div class="select-menu-item-text js-select-button-text">All repositories</div>
          </div> <!-- /.select-menu-item -->

        </div>
      </div>
    </div>

  <span class="octicon help tooltipped downwards" title="Show command bar help">
    <span class="octicon octicon-question"></span>
  </span>


  <input type="hidden" name="ref" value="cmdform">

</form>
    </div>

  </div>
</div>


      


          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        

<ul class="pagehead-actions">


  <li>
    <a href="/login?return_to=%2FTKJElectronics%2FExample-Sketch-for-IMU-including-Kalman-filter"
    class="minibutton with-count js-toggler-target star-button tooltipped upwards"
    title="You must be signed in to use this feature" rel="nofollow">
    <span class="octicon octicon-star"></span>Star
  </a>

    <a class="social-count js-social-count" href="/TKJElectronics/Example-Sketch-for-IMU-including-Kalman-filter/stargazers">
      34
    </a>

  </li>

    <li>
      <a href="/login?return_to=%2FTKJElectronics%2FExample-Sketch-for-IMU-including-Kalman-filter"
        class="minibutton with-count js-toggler-target fork-button tooltipped upwards"
        title="You must be signed in to fork a repository" rel="nofollow">
        <span class="octicon octicon-git-branch"></span>Fork
      </a>
      <a href="/TKJElectronics/Example-Sketch-for-IMU-including-Kalman-filter/network" class="social-count">
        60
      </a>
    </li>
</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="repo-label"><span>public</span></span>
          <span class="mega-octicon octicon-repo"></span>
          <span class="author">
            <a href="/TKJElectronics" class="url fn" itemprop="url" rel="author"><span itemprop="title">TKJElectronics</span></a>
          </span>
          <span class="repohead-name-divider">/</span>
          <strong><a href="/TKJElectronics/Example-Sketch-for-IMU-including-Kalman-filter" class="js-current-repository js-repo-home-link">Example-Sketch-for-IMU-including-Kalman-filter</a></strong>

          <span class="page-context-loader">
            <img alt="Octocat-spinner-32" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">
      

      <div class="repository-with-sidebar repo-container new-discussion-timeline js-new-discussion-timeline  ">
        <div class="repository-sidebar">
            

<div class="sunken-menu vertical-right repo-nav js-repo-nav js-repository-container-pjax js-octicon-loaders">
  <div class="sunken-menu-contents">
    <ul class="sunken-menu-group">
      <li class="tooltipped leftwards" title="Code">
        <a href="/TKJElectronics/Example-Sketch-for-IMU-including-Kalman-filter" aria-label="Code" class="selected js-selected-navigation-item sunken-menu-item" data-gotokey="c" data-pjax="true" data-selected-links="repo_source repo_downloads repo_commits repo_tags repo_branches /TKJElectronics/Example-Sketch-for-IMU-including-Kalman-filter">
          <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

        <li class="tooltipped leftwards" title="Issues">
          <a href="/TKJElectronics/Example-Sketch-for-IMU-including-Kalman-filter/issues" aria-label="Issues" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-gotokey="i" data-selected-links="repo_issues /TKJElectronics/Example-Sketch-for-IMU-including-Kalman-filter/issues">
            <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
            <span class='counter'>1</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>

      <li class="tooltipped leftwards" title="Pull Requests">
        <a href="/TKJElectronics/Example-Sketch-for-IMU-including-Kalman-filter/pulls" aria-label="Pull Requests" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-gotokey="p" data-selected-links="repo_pulls /TKJElectronics/Example-Sketch-for-IMU-including-Kalman-filter/pulls">
            <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull Requests</span>
            <span class='counter'>1</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>


    </ul>
    <div class="sunken-menu-separator"></div>
    <ul class="sunken-menu-group">

      <li class="tooltipped leftwards" title="Pulse">
        <a href="/TKJElectronics/Example-Sketch-for-IMU-including-Kalman-filter/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="pulse /TKJElectronics/Example-Sketch-for-IMU-including-Kalman-filter/pulse">
          <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped leftwards" title="Graphs">
        <a href="/TKJElectronics/Example-Sketch-for-IMU-including-Kalman-filter/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="repo_graphs repo_contributors /TKJElectronics/Example-Sketch-for-IMU-including-Kalman-filter/graphs">
          <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped leftwards" title="Network">
        <a href="/TKJElectronics/Example-Sketch-for-IMU-including-Kalman-filter/network" aria-label="Network" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-selected-links="repo_network /TKJElectronics/Example-Sketch-for-IMU-including-Kalman-filter/network">
          <span class="octicon octicon-git-branch"></span> <span class="full-word">Network</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>
    </ul>


  </div>
</div>

              <div class="only-with-full-nav">
                

  

<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone">
  <h3><strong>HTTPS</strong> clone URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/TKJElectronics/Example-Sketch-for-IMU-including-Kalman-filter.git" readonly="readonly">

    <span class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="https://github.com/TKJElectronics/Example-Sketch-for-IMU-including-Kalman-filter.git" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>

  

<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone">
  <h3><strong>Subversion</strong> checkout URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/TKJElectronics/Example-Sketch-for-IMU-including-Kalman-filter" readonly="readonly">

    <span class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="https://github.com/TKJElectronics/Example-Sketch-for-IMU-including-Kalman-filter" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>


<p class="clone-options">You can clone with
      <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>,
      or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <span class="octicon help tooltipped upwards" title="Get help on which URL is right for you.">
    <a href="https://help.github.com/articles/which-remote-url-should-i-use">
    <span class="octicon octicon-question"></span>
    </a>
  </span>
</p>


  <a href="http://windows.github.com" class="minibutton sidebar-button">
    <span class="octicon octicon-device-desktop"></span>
    Clone in Desktop
  </a>

                <a href="/TKJElectronics/Example-Sketch-for-IMU-including-Kalman-filter/archive/master.zip"
                   class="minibutton sidebar-button"
                   title="Download this repository as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
              </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          


<!-- blob contrib key: blob_contributors:v21:798ce097f56d771362793a793935ea53 -->

<p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

<a href="/TKJElectronics/Example-Sketch-for-IMU-including-Kalman-filter/find/master" data-pjax data-hotkey="t" class="js-show-file-finder" style="display:none">Show File Finder</a>

<div class="file-navigation">
  

<div class="select-menu js-menu-container js-select-menu" >
  <span class="minibutton select-menu-button js-menu-target" data-hotkey="w"
    data-master-branch="master"
    data-ref="master"
    role="button" aria-label="Switch branches or tags" tabindex="0">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax>

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-remove-close js-menu-close"></span>
      </div> <!-- /.select-menu-header -->

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div><!-- /.select-menu-tabs -->
      </div><!-- /.select-menu-filters -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/TKJElectronics/Example-Sketch-for-IMU-including-Kalman-filter/blob/master/README.md"
                 data-name="master"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="master">master</a>
            </div> <!-- /.select-menu-item -->
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

    </div> <!-- /.select-menu-modal -->
  </div> <!-- /.select-menu-modal-holder -->
</div> <!-- /.select-menu -->

  <div class="breadcrumb">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/TKJElectronics/Example-Sketch-for-IMU-including-Kalman-filter" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">Example-Sketch-for-IMU-including-Kalman-filter</span></a></span></span><span class="separator"> / </span><strong class="final-path">README.md</strong> <span class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="README.md" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>


  <div class="commit file-history-tease">
    <img alt="Kristian Sloth Lauszus" class="main-avatar" height="24" src="https://2.gravatar.com/avatar/04aa3aec79f1845a03eeb74681b57204?d=https%3A%2F%2Fidenticons.github.com%2Fe27489e2fb462efafc0a30d7445e5bcd.png&amp;r=x&amp;s=140" width="24" />
    <span class="author"><a href="/Lauszus" rel="author">Lauszus</a></span>
    <time class="js-relative-date" datetime="2013-08-26T07:59:18-07:00" title="2013-08-26 07:59:18">August 26, 2013</time>
    <div class="commit-title">
        <a href="/TKJElectronics/Example-Sketch-for-IMU-including-Kalman-filter/commit/51ac9a568cb3ae7f6186fdee26643ef2ea0fcf67" class="message" data-pjax="true" title="Updated readme">Updated readme</a>
    </div>

    <div class="participation">
      <p class="quickstat"><a href="#blob_contributors_box" rel="facebox"><strong>1</strong> contributor</a></p>
      
    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list">
          <li class="facebox-user-list-item">
            <img alt="Kristian Sloth Lauszus" height="24" src="https://2.gravatar.com/avatar/04aa3aec79f1845a03eeb74681b57204?d=https%3A%2F%2Fidenticons.github.com%2Fe27489e2fb462efafc0a30d7445e5bcd.png&amp;r=x&amp;s=140" width="24" />
            <a href="/Lauszus">Lauszus</a>
          </li>
      </ul>
    </div>
  </div>

<div id="files" class="bubble">
  <div class="file">
    <div class="meta">
      <div class="info">
        <span class="icon"><b class="octicon octicon-file-text"></b></span>
        <span class="mode" title="File Mode">file</span>
          <span>16 lines (10 sloc)</span>
        <span>0.979 kb</span>
      </div>
      <div class="actions">
        <div class="button-group">
            <a class="minibutton tooltipped leftwards"
               href="http://windows.github.com" title="Open this file in GitHub for Windows">
                <span class="octicon octicon-device-desktop"></span> Open
            </a>
              <a class="minibutton disabled tooltipped leftwards" href="#"
                 title="You must be signed in to make or propose changes">Edit</a>
          <a href="/TKJElectronics/Example-Sketch-for-IMU-including-Kalman-filter/raw/master/README.md" class="button minibutton " id="raw-url">Raw</a>
            <a href="/TKJElectronics/Example-Sketch-for-IMU-including-Kalman-filter/blame/master/README.md" class="button minibutton js-update-url-with-hash">Blame</a>
          <a href="/TKJElectronics/Example-Sketch-for-IMU-including-Kalman-filter/commits/master/README.md" class="button minibutton " rel="nofollow">History</a>
        </div><!-- /.button-group -->
          <a class="minibutton danger disabled empty-icon tooltipped leftwards" href="#"
             title="You must be signed in to make or propose changes">
          Delete
        </a>
      </div><!-- /.actions -->
    </div>
      
  <div id="readme" class="blob instapaper_body">
    <article class="markdown-body entry-content" itemprop="mainContentOfPage"><h4>
<a name="developed-by-kristian-lauszus-tkj-electronics-2012" class="anchor" href="#developed-by-kristian-lauszus-tkj-electronics-2012"><span class="octicon octicon-link"></span></a>Developed by Kristian Lauszus, TKJ Electronics 2012</h4>

<p>The code is released under the GNU General Public License.</p>

<hr><p>This is the firmware for the my guide at the Arduino forum: <a href="http://arduino.cc/forum/index.php/topic,58048.0.html">http://arduino.cc/forum/index.php/topic,58048.0.html</a>, including a Processing application (see the <a href="/TKJElectronics/Example-Sketch-for-IMU-including-Kalman-filter/blob/master/Graph">Graph</a> directory) to visualize the data sent from the Arduino.</p>

<p>There is currently examples for the following IMU's:</p>

<ul>
<li>"IMU Analog Combo Board Razor - 6DOF Ultra-Thin IMU" from Sparkfun: <a href="http://www.sparkfun.com/products/10010">http://www.sparkfun.com/products/10010</a>
</li>
<li>Digital IMU featuring a ITG3205 and a ADXL345</li>
<li>MPU-6050 - 3-axis gyroscope and 3-axis accelerometer</li>
</ul><p>The Kalman filter used in all the examples can be found at my other repository: <a href="https://github.com/TKJElectronics/KalmanFilter">https://github.com/TKJElectronics/KalmanFilter</a>.</p>

<p>For more information fell free to post a question at the guide: <a href="http://arduino.cc/forum/index.php/topic,58048.0.html">http://arduino.cc/forum/index.php/topic,58048.0.html</a> or send me an email at <a href="mailto:kristianl@tkjelectronics.dk"></a><a href="mailto:kristianl@tkjelectronics.dk">kristianl@tkjelectronics.dk</a>.</p></article>
  </div>

  </div>
</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" class="js-jump-to-line-form">
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="button">Go</button>
  </form>
</div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer">
    <ul class="site-footer-links right">
      <li><a href="https://status.github.com/">Status</a></li>
      <li><a href="http://developer.github.com">API</a></li>
      <li><a href="http://training.github.com">Training</a></li>
      <li><a href="http://shop.github.com">Shop</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/about">About</a></li>

    </ul>

    <a href="/">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
    </a>

    <ul class="site-footer-links">
      <li>&copy; 2014 <span title="0.02058s from github-fe137-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="/site/terms">Terms</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
  </div><!-- /.site-footer -->
</div><!-- /.container -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
          <div class="suggester-container">
              <div class="suggester fullscreen-suggester js-navigation-container" id="fullscreen_suggester"
                 data-url="/TKJElectronics/Example-Sketch-for-IMU-including-Kalman-filter/suggestions/commit">
              </div>
          </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped leftwards" title="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped leftwards"
      title="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-remove-close close js-ajax-error-dismiss"></a>
      Something went wrong with that request. Please try again.
    </div>

  </body>
</html>

