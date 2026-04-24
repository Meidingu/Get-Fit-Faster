import re

with open(r'C:\Users\ajaok\OneDrive\Desktop\FitnessApp\frontend\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print(f'File loaded, length: {len(html)}')
print(f'Has AUTH SCREEN marker: {"AUTH SCREEN" in html}')

# =========================================================
# PART 1: Replace the VIDEO BACKGROUND container + overlay
# with the new cinematic sandy background + runner gradient
# =========================================================

old_video_section = '''  <!-- VIDEO BACKGROUND -->
  <div id="video-bg-container">
    <video autoplay loop muted playsinline>
      <source src="/fitness_background.mp4" type="video/mp4">
    </video>
  </div>
  <div class="spline-overlay"></div>'''

new_video_section = '''  <!-- CINEMATIC HERO BACKGROUND -->
  <div id="hero-bg">
    <div class="hero-bg-gradient"></div>
    <div class="hero-runner-silhouette"></div>
  </div>'''

if old_video_section in html:
    html = html.replace(old_video_section, new_video_section)
    print('✓ Video section replaced')
else:
    print('✗ Video section NOT found - trying fallback...')
    # Try without the exact spacing
    if 'video-bg-container' in html:
        print('  video-bg-container exists in HTML')

# =========================================================
# PART 2: Replace the entire auth screen HTML
# =========================================================

old_auth_html = '''  <div id="auth-screen">
    <div class="auth-left">
      <div class="auth-bg"></div>
      <div class="auth-brand anim-fade-up">
        <div class="auth-logo">GET<span> FIT</span></div>
        <div class="auth-tagline">FASTER. STRONGER. EVERY DAY.</div>
        <div class="auth-feat">
          <div class="auth-feat-item">
            <div class="auth-feat-dot"></div>
            <div class="auth-feat-label">AI Activity Detection</div>
          </div>
          <div class="auth-feat-item">
            <div class="auth-feat-dot"></div>
            <div class="auth-feat-label">Calorie Tracking</div>
          </div>
          <div class="auth-feat-item">
            <div class="auth-feat-dot"></div>
            <div class="auth-feat-label">Workout Plans</div>
          </div>
          <div class="auth-feat-item">
            <div class="auth-feat-dot"></div>
            <div class="auth-feat-label">Body Analytics</div>
          </div>
        </div>
      </div>
    </div>

    <div class="auth-right">
      <div class="auth-card anim-slide-left">
        <div class="auth-switch">
          <button class="auth-switch-btn active" onclick="authTab('login')">Login</button>
          <button class="auth-switch-btn" onclick="authTab('register')">Register</button>
        </div>

        <div id="form-login">
          <div class="auth-form-title">WELCOME<br>BACK.</div>
          <div class="auth-form-sub">ENTER YOUR CREDENTIALS TO CONTINUE</div>
          <div class="auth-err" id="login-err"></div>
          <div class="field"><label class="field-label">Email address</label><input class="field-input" id="l-email"
              type="email" placeholder="you@email.com"></div>
          <div class="field"><label class="field-label">Password</label><input class="field-input" id="l-pass"
              type="password" placeholder="••••••••"></div>
          <button class="btn-volt" onclick="doLogin()">LOG IN →</button>
        </div>

        <div id="form-register" style="display:none">
          <div class="auth-form-title">JOIN<br>TODAY.</div>
          <div class="auth-form-sub">START YOUR FITNESS JOURNEY NOW</div>
          <div class="auth-err" id="reg-err"></div>
          <div class="field"><label class="field-label">Full name</label><input class="field-input" id="r-name"
              placeholder="Your name"></div>
          <div class="field"><label class="field-label">Email address</label><input class="field-input" id="r-email"
              type="email" placeholder="you@email.com"></div>
          <div class="field"><label class="field-label">Password (min 6 chars)</label><input class="field-input"
              id="r-pass" type="password" placeholder="••••••••"></div>
          <button class="btn-volt" onclick="doRegister()">CREATE ACCOUNT →</button>
        </div>
      </div>
    </div>
  </div>'''

new_auth_html = '''  <div id="auth-screen">
    <!-- Cinematic typography layer -->
    <div class="hero-typography">
      <div class="hero-word hero-track">track</div>
      <div class="hero-slash-group">
        <span class="hero-slash">/</span><span class="hero-your">your</span>
      </div>
      <div class="hero-activity">activity</div>
    </div>

    <!-- Phone mockup -->
    <div class="hero-phone">
      <div class="phone-card">
        <div class="phone-label">YOU RUN TODAY</div>
        <div class="phone-km">10.73 <span>KM</span></div>
        <div class="phone-map">
          <svg viewBox="0 0 160 120" fill="none" xmlns="http://www.w3.org/2000/svg">
            <polyline points="30,100 40,85 35,70 50,60 45,42 60,30 75,38 80,28 95,22 105,35 115,28 130,40 125,55 135,68 120,80 110,90 95,100 80,95 65,105 50,98 38,110" stroke="white" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" fill="none" stroke-dasharray="400" class="route-line"/>
            <circle cx="30" cy="100" r="4" fill="#ff6600"/>
            <circle cx="130" cy="40" r="3" fill="white" opacity="0.6"/>
          </svg>
          <div class="map-location">SILICON<br>VALLEY</div>
        </div>
        <div class="phone-stats">
          <div class="phone-stat">
            <div class="phone-stat-label">PACE</div>
            <div class="phone-stat-val">3:23<span>/KM</span></div>
          </div>
          <div class="phone-stat">
            <div class="phone-stat-label">TIME</div>
            <div class="phone-stat-val">42:22</div>
          </div>
          <div class="phone-stat">
            <div class="phone-stat-label">ENERGY</div>
            <div class="phone-stat-val">135<span>KCAL</span></div>
          </div>
        </div>
      </div>
    </div>

    <!-- Bottom social row -->
    <div class="hero-social">
      <div class="hero-social-left">
        <span class="social-label">RUN WITH</span>
        <div class="social-avatars">
          <div class="avatar av1"></div>
          <div class="avatar av2"></div>
          <div class="avatar av3"></div>
        </div>
        <span class="social-label">FRIENDS</span>
      </div>
      <div class="hero-social-right">
        Running with friends can be a fantastic way to stay motivated and enjoy the outdoors.
      </div>
    </div>

    <!-- Login form - floating panel -->
    <div class="auth-panel">
      <div class="auth-panel-inner">
        <div class="auth-brand-mini">
          <span class="brand-dot"></span>
          <span class="brand-name">GET FIT</span>
        </div>
        <div class="auth-switch">
          <button class="auth-switch-btn active" onclick="authTab('login')">Login</button>
          <button class="auth-switch-btn" onclick="authTab('register')">Register</button>
        </div>

        <div id="form-login">
          <div class="auth-form-title">Welcome<br><em>back.</em></div>
          <div class="auth-form-sub">Enter your credentials to continue</div>
          <div class="auth-err" id="login-err"></div>
          <div class="field"><label class="field-label">Email address</label><input class="field-input" id="l-email"
              type="email" placeholder="you@email.com"></div>
          <div class="field"><label class="field-label">Password</label><input class="field-input" id="l-pass"
              type="password" placeholder="••••••••"></div>
          <button class="btn-volt" onclick="doLogin()">Start Running →</button>
        </div>

        <div id="form-register" style="display:none">
          <div class="auth-form-title">Join<br><em>today.</em></div>
          <div class="auth-form-sub">Start your fitness journey now</div>
          <div class="auth-err" id="reg-err"></div>
          <div class="field"><label class="field-label">Full name</label><input class="field-input" id="r-name"
              placeholder="Your name"></div>
          <div class="field"><label class="field-label">Email address</label><input class="field-input" id="r-email"
              type="email" placeholder="you@email.com"></div>
          <div class="field"><label class="field-label">Password (min 6 chars)</label><input class="field-input"
              id="r-pass" type="password" placeholder="••••••••"></div>
          <button class="btn-volt" onclick="doRegister()">Create Account →</button>
        </div>
      </div>
    </div>
  </div>'''

# Try to find auth screen in html
if '<div id="auth-screen">' in html:
    # Find start
    start_idx = html.index('<div id="auth-screen">')
    # Find the matching close: look for </div>\n\n  <div id="app-screen"
    end_marker = '<div id="app-screen">'
    end_idx = html.index(end_marker)
    # Go backward to find the closing div
    section = html[start_idx:end_idx]
    # Replace
    html = html[:start_idx] + new_auth_html + '\n\n  ' + html[end_idx:]
    print('✓ Auth screen HTML replaced')
else:
    print('✗ Auth screen div NOT found')

# =========================================================
# PART 3: Save updated file
# =========================================================
with open(r'C:\Users\ajaok\OneDrive\Desktop\FitnessApp\frontend\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'✓ File saved, new length: {len(html)}')
