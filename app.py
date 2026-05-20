from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Steland Construction</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;600&family=Bebas+Neue&family=DM+Sans:wght@300;400&display=swap" rel="stylesheet">
<style>
  *, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }

  :root {
    --black: #0a0a0a;
    --white: #f5f0eb;
    --gold: #c9a84c;
    --gold-light: #e8d5a3;
    --grey: #2a2a2a;
    --mid: #6b6b6b;
  }

  html { scroll-behavior: smooth; }

  body {
    background: var(--black);
    color: var(--white);
    font-family: 'DM Sans', sans-serif;
    font-weight: 300;
    overflow-x: hidden;
  }

  /* NAV */
  nav {
    position: fixed; top: 0; left: 0; right: 0; z-index: 100;
    display: flex; justify-content: space-between; align-items: center;
    padding: 1.5rem 4rem;
    background: linear-gradient(to bottom, rgba(10,10,10,0.95), transparent);
  }

  .logo {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 2rem;
    letter-spacing: 0.3em;
    color: var(--gold);
    text-decoration: none;
  }

  nav ul { list-style: none; display: flex; gap: 3rem; }
  nav ul a {
    color: var(--white);
    text-decoration: none;
    font-size: 0.8rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    opacity: 0.8;
    transition: opacity 0.3s, color 0.3s;
  }
  nav ul a:hover { opacity: 1; color: var(--gold); }

  /* LANG TOGGLE */
  .lang-toggle {
    display: flex;
    align-items: center;
    gap: 0;
    border: 1px solid var(--gold);
    overflow: hidden;
    flex-shrink: 0;
  }
  .lang-toggle button {
    background: transparent;
    border: none;
    color: var(--white);
    font-family: 'DM Sans', sans-serif;
    font-size: 0.72rem;
    letter-spacing: 0.15em;
    padding: 0.4rem 0.75rem;
    cursor: pointer;
    opacity: 0.55;
    transition: all 0.25s;
  }
  .lang-toggle button.active {
    background: var(--gold);
    color: var(--black);
    opacity: 1;
  }
  .lang-toggle button:not(.active):hover { opacity: 1; color: var(--gold); }
  .lang-sep { width: 1px; background: var(--gold); height: 24px; flex-shrink: 0; }

  /* HERO */
  .hero {
    height: 100vh;
    position: relative;
    display: flex; align-items: center;
    overflow: hidden;
  }

  .hero-bg {
    position: absolute; inset: 0;
    background:
      linear-gradient(to right, rgba(10,10,10,0.85) 40%, rgba(10,10,10,0.3)),
      url('https://images.unsplash.com/photo-1486325212027-8081e485255e?w=1800&q=80') center/cover;
    animation: slowZoom 20s ease-in-out infinite alternate;
  }

  @keyframes slowZoom {
    from { transform: scale(1); }
    to   { transform: scale(1.06); }
  }

  .hero-content {
    position: relative; z-index: 2;
    padding: 0 4rem;
    max-width: 750px;
    animation: fadeUp 1.2s ease both;
  }

  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(40px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  .hero-tag {
    font-size: 0.75rem;
    letter-spacing: 0.4em;
    text-transform: uppercase;
    color: var(--gold);
    margin-bottom: 1.5rem;
    display: flex; align-items: center; gap: 1rem;
  }
  .hero-tag::before {
    content: '';
    display: block; width: 40px; height: 1px;
    background: var(--gold);
  }

  .hero h1 {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(3.5rem, 8vw, 7rem);
    font-weight: 300;
    line-height: 1.05;
    margin-bottom: 2rem;
  }

  .hero h1 em {
    font-style: italic;
    color: var(--gold-light);
  }

  .hero p {
    font-size: 1rem;
    line-height: 1.8;
    opacity: 0.75;
    max-width: 480px;
    margin-bottom: 3rem;
  }

  .btn {
    display: inline-block;
    padding: 1rem 2.5rem;
    border: 1px solid var(--gold);
    color: var(--gold);
    text-decoration: none;
    font-size: 0.75rem;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    transition: all 0.3s;
  }
  .btn:hover {
    background: var(--gold);
    color: var(--black);
  }

  /* DIVIDER */
  .divider {
    display: flex; align-items: center; gap: 2rem;
    padding: 0 4rem;
    margin: 5rem 0 3rem;
  }
  .divider span {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 0.9rem;
    letter-spacing: 0.4em;
    color: var(--gold);
  }
  .divider::before, .divider::after {
    content: ''; flex: 1; height: 1px;
    background: linear-gradient(to right, transparent, var(--gold), transparent);
  }

  /* SERVICES */
  #services { padding: 5rem 4rem; }

  .section-label {
    font-size: 0.7rem;
    letter-spacing: 0.5em;
    text-transform: uppercase;
    color: var(--gold);
    margin-bottom: 1rem;
  }

  .section-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(2.5rem, 5vw, 4rem);
    font-weight: 300;
    margin-bottom: 4rem;
    max-width: 600px;
  }

  .services-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2px;
  }

  .service-card {
    position: relative;
    height: 380px;
    overflow: hidden;
    cursor: pointer;
  }

  .service-card img {
    width: 100%; height: 100%;
    object-fit: cover;
    transition: transform 0.7s ease;
    filter: brightness(0.55);
  }

  .service-card:hover img {
    transform: scale(1.08);
    filter: brightness(0.4);
  }

  .service-info {
    position: absolute; inset: 0;
    display: flex; flex-direction: column;
    justify-content: flex-end;
    padding: 2rem;
    background: linear-gradient(to top, rgba(0,0,0,0.8) 0%, transparent 60%);
  }

  .service-num {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 3rem;
    color: var(--gold);
    opacity: 0.3;
    line-height: 1;
    margin-bottom: 0.5rem;
  }

  .service-name {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.8rem;
    font-weight: 400;
    margin-bottom: 0.5rem;
  }

  .service-desc {
    font-size: 0.8rem;
    opacity: 0;
    transform: translateY(10px);
    transition: all 0.4s ease;
    line-height: 1.7;
    color: var(--gold-light);
  }

  .service-card:hover .service-desc {
    opacity: 1;
    transform: translateY(0);
  }

  /* ABOUT */
  #about {
    padding: 6rem 4rem;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6rem;
    align-items: center;
  }

  .about-img-wrap {
    position: relative;
    height: 600px;
  }

  .about-img-wrap img {
    width: 100%; height: 100%;
    object-fit: cover;
  }

  .about-img-wrap::after {
    content: '';
    position: absolute;
    bottom: -20px; right: -20px;
    width: 60%; height: 60%;
    border: 1px solid var(--gold);
    z-index: -1;
  }

  .about-text .section-title { margin-bottom: 2rem; }

  .about-text p {
    opacity: 0.75;
    line-height: 1.9;
    margin-bottom: 1.5rem;
    font-size: 0.95rem;
  }

  .stats {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2rem;
    margin: 3rem 0;
    padding: 2rem 0;
    border-top: 1px solid rgba(201,168,76,0.2);
    border-bottom: 1px solid rgba(201,168,76,0.2);
  }

  .stat-num {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 3rem;
    color: var(--gold);
    line-height: 1;
  }

  .stat-label {
    font-size: 0.75rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    opacity: 0.6;
    margin-top: 0.3rem;
  }

  /* GALLERY */
  #gallery { padding: 5rem 4rem; }

  .gallery-grid {
    display: grid;
    grid-template-columns: 2fr 1fr 1fr;
    grid-template-rows: 300px 300px;
    gap: 4px;
    margin-top: 3rem;
  }

  .gallery-grid img {
    width: 100%; height: 100%;
    object-fit: cover;
    transition: filter 0.4s;
    filter: grayscale(20%);
  }

  .gallery-grid img:hover { filter: grayscale(0%) brightness(1.1); }

  .gallery-grid .span-col { grid-row: span 2; }

  /* CONTACT */
  #contact {
    padding: 6rem 4rem;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6rem;
    background: var(--grey);
  }

  .contact-left h2 {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(2.5rem, 5vw, 4rem);
    font-weight: 300;
    margin-bottom: 2rem;
    line-height: 1.1;
  }

  .contact-item {
    display: flex; align-items: flex-start;
    gap: 1.5rem;
    margin-bottom: 2rem;
    padding-bottom: 2rem;
    border-bottom: 1px solid rgba(255,255,255,0.08);
  }

  .contact-icon {
    width: 40px; height: 40px;
    border: 1px solid var(--gold);
    display: flex; align-items: center; justify-content: center;
    color: var(--gold);
    font-size: 1rem;
    flex-shrink: 0;
  }

  .contact-label {
    font-size: 0.7rem;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    color: var(--gold);
    margin-bottom: 0.3rem;
  }

  .contact-value {
    font-size: 0.95rem;
    opacity: 0.85;
  }

  .contact-form { display: flex; flex-direction: column; gap: 1.5rem; }

  .form-group { display: flex; flex-direction: column; gap: 0.5rem; }

  .form-group label {
    font-size: 0.7rem;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    color: var(--gold);
  }

  .form-group input,
  .form-group textarea,
  .form-group select {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.12);
    color: var(--white);
    padding: 0.9rem 1.2rem;
    font-family: 'DM Sans', sans-serif;
    font-size: 0.9rem;
    outline: none;
    transition: border-color 0.3s;
  }

  .form-group input:focus,
  .form-group textarea:focus,
  .form-group select:focus {
    border-color: var(--gold);
  }

  .form-group select option { background: var(--grey); }

  .form-group textarea { height: 120px; resize: vertical; }

  .btn-submit {
    background: var(--gold);
    color: var(--black);
    border: none;
    padding: 1rem 2.5rem;
    font-family: 'DM Sans', sans-serif;
    font-size: 0.8rem;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    cursor: pointer;
    transition: opacity 0.3s;
    align-self: flex-start;
  }
  .btn-submit:hover { opacity: 0.85; }

  /* FOOTER */
  footer {
    padding: 2rem 4rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid rgba(255,255,255,0.08);
    font-size: 0.75rem;
    opacity: 0.5;
  }

  /* SCROLL FADE */
  .fade-in {
    opacity: 0;
    transform: translateY(30px);
    transition: opacity 0.8s ease, transform 0.8s ease;
  }
  .fade-in.visible {
    opacity: 1;
    transform: translateY(0);
  }

  @media (max-width: 900px) {
    nav { padding: 1.5rem 2rem; }
    nav ul { gap: 1.5rem; }
    .hero-content { padding: 0 2rem; }
    #services, #gallery, #about, #contact { padding: 4rem 2rem; }
    #about, #contact { grid-template-columns: 1fr; gap: 3rem; }
    .gallery-grid { grid-template-columns: 1fr 1fr; grid-template-rows: auto; }
    .gallery-grid .span-col { grid-row: span 1; }
    .divider { padding: 0 2rem; }
  }
</style>
</head>
<body>

<nav>
  <a href="#"><img src="/static/logo.png" height="140" alt="Steland" style="border-radius:8px;"></a>
  <ul>
    <li><a href="#services" data-zh="服务" data-en="Services">服务</a></li>
    <li><a href="#about" data-zh="关于" data-en="About">关于</a></li>
    <li><a href="#gallery" data-zh="项目" data-en="Projects">项目</a></li>
    <li><a href="#contact" data-zh="联系" data-en="Contact">联系</a></li>
  </ul>
  <div class="lang-toggle">
    <button id="btn-zh" class="active" onclick="setLang('zh')">中文</button>
    <div class="lang-sep"></div>
    <button id="btn-en" onclick="setLang('en')">EN</button>
  </div>
</nav>

<!-- HERO -->
<section class="hero">
  <div class="hero-bg"></div>
  <div class="hero-content">
    <div class="hero-tag">Premium Construction & Renovation</div>
    <h1 data-zh="建筑之美<br><em>源于匠心</em>" data-en="Building <em>Excellence</em><br>From the Ground Up">建筑之美<br><em>源于匠心</em></h1>
    <p data-zh="Steland 专注于高端建筑与改造服务，将您的设计愿景转化为卓越的现实空间。每一个项目，都是一件艺术品。"
       data-en="Steland specialises in premium construction and renovation, transforming your vision into extraordinary spaces. Every project is a masterpiece.">
      Steland 专注于高端建筑与改造服务，将您的设计愿景转化为卓越的现实空间。每一个项目，都是一件艺术品。
    </p>
    <a href="#contact" class="btn" data-zh="免费咨询" data-en="Free Consultation">免费咨询</a>
  </div>
</section>

<!-- SERVICES -->
<div class="divider"><span data-zh="我们的服务" data-en="Our Services">我们的服务</span></div>
<section id="services">
  <p class="section-label">What We Do</p>
  <h2 class="section-title" data-zh="专业建筑服务<br>全方位解决方案" data-en="Professional Services<br>End-to-End Solutions">专业建筑服务<br>全方位解决方案</h2>

  <div class="services-grid">
    <div class="service-card">
      <img src="https://images.unsplash.com/photo-1581578731548-c64695cc6952?w=800&q=80" alt="Interior">
      <div class="service-info">
        <div class="service-num">01</div>
        <div class="service-name" data-zh="室内装修" data-en="Interior Fitout">室内装修</div>
        <div class="service-desc" data-zh="专业室内装修团队，精选材料，打造高品质生活空间。" data-en="Expert interior fitout team using premium materials to create high-quality living spaces.">专业室内装修团队，精选材料，打造高品质生活空间。</div>
      </div>
    </div>
    <div class="service-card">
      <img src="https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=800&q=80" alt="Renovation">
      <div class="service-info">
        <div class="service-num">02</div>
        <div class="service-name" data-zh="空间改建" data-en="Renovation">空间改建</div>
        <div class="service-desc" data-zh="重新规划空间布局，提升功能性与美观度。" data-en="Redesigning spatial layouts to enhance functionality and visual appeal.">重新规划空间布局，提升功能性与美观度。</div>
      </div>
    </div>
    <div class="service-card">
      <img src="https://images.unsplash.com/photo-1429497419816-9ca5cfb4571a?w=800&q=80" alt="Extension">
      <div class="service-info">
        <div class="service-num">03</div>
        <div class="service-name" data-zh="扩建加建" data-en="Extensions">扩建加建</div>
        <div class="service-desc" data-zh="扩展现有建筑面积，提供更多实用空间。" data-en="Expanding your existing footprint to create more practical, usable space.">扩展现有建筑面积，提供更多实用空间。</div>
      </div>
    </div>
    <div class="service-card">
      <img src="https://images.unsplash.com/photo-1523217582562-09d0def993a6?w=800&q=80" alt="Restoration">
      <div class="service-info">
        <div class="service-num">04</div>
        <div class="service-name" data-zh="建筑翻新" data-en="Restoration">建筑翻新</div>
        <div class="service-desc" data-zh="焕新老旧建筑，保留历史风貌，注入现代活力。" data-en="Breathing new life into existing buildings while preserving their character.">焕新老旧建筑，保留历史风貌，注入现代活力。</div>
      </div>
    </div>
    <div class="service-card">
      <img src="https://images.unsplash.com/photo-1503387762-592deb58ef4e?w=800&q=80" alt="New Build">
      <div class="service-info">
        <div class="service-num">05</div>
        <div class="service-name" data-zh="新建项目" data-en="New Builds">新建项目</div>
        <div class="service-desc" data-zh="从零开始，按您的设计理念，建造梦想建筑。" data-en="Building your dream from the ground up, exactly as you envision it.">从零开始，按您的设计理念，建造梦想建筑。</div>
      </div>
    </div>
  </div>
</section>

<!-- ABOUT -->
<section id="about" class="fade-in">
  <div class="about-img-wrap">
    <img src="/static/about.jpg" alt="Steland Building">
  </div>
  <div class="about-text">
    <p class="section-label">About Steland</p>
    <h2 class="section-title" data-zh="专注建筑<br>追求卓越" data-en="Dedicated to<br>Excellence">专注建筑<br>追求卓越</h2>
    <p data-zh="Steland 是一家专注于高品质建筑与改造服务的公司，拥有丰富的项目经验和专业的施工团队。我们相信，每一栋建筑都有其独特的故事。"
       data-en="Steland is a company dedicated to high-quality construction and renovation services, with extensive project experience and a professional construction team. We believe every building has its own unique story.">
      Steland 是一家专注于高品质建筑与改造服务的公司，拥有丰富的项目经验和专业的施工团队。我们相信，每一栋建筑都有其独特的故事。
    </p>
    <p data-zh="从初步规划到最终交付，我们全程负责，确保每个细节都符合最高标准。客户满意是我们最大的追求。"
       data-en="From initial planning through to final handover, we take full ownership of every detail to meet the highest standards. Client satisfaction is our greatest pursuit.">
      从初步规划到最终交付，我们全程负责，确保每个细节都符合最高标准。客户满意是我们最大的追求。
    </p>
    <div class="stats">
      <div>
        <div class="stat-num">10+</div>
        <div class="stat-label" data-zh="年行业经验" data-en="Years Experience">年行业经验</div>
      </div>
      <div>
        <div class="stat-num">50+</div>
        <div class="stat-label" data-zh="完成项目" data-en="Projects Completed">完成项目</div>
      </div>
      <div>
        <div class="stat-num">98%</div>
        <div class="stat-label" data-zh="客户满意度" data-en="Client Satisfaction">客户满意度</div>
      </div>
    </div>
    <a href="#contact" class="btn" data-zh="与我们合作" data-en="Work With Us">与我们合作</a>
  </div>
</section>

<!-- GALLERY -->
<section id="gallery" class="fade-in">
  <p class="section-label">Our Projects</p>
  <h2 class="section-title" data-zh="精选项目" data-en="Featured Projects">精选项目</h2>
  <div class="gallery-grid">
    <img class="span-col" src="/static/1.png" alt="Project 1">
    <img src="/static/2.png" alt="Project 2">
    <img src="/static/3.png" alt="Project 3">
    <img src="/static/4.png" alt="Project 4">
    <img src="/static/5.jpg" alt="Project 5">
  </div>
</section>

<!-- CONTACT -->
<section id="contact" class="fade-in">
  <div class="contact-left">
    <p class="section-label">Get In Touch</p>
    <h2 data-zh="让我们开始<br>您的项目" data-en="Let's Start<br>Your Project">让我们开始<br>您的项目</h2>

    <div class="contact-item">
      <div class="contact-icon">✉</div>
      <div>
        <div class="contact-label">Email</div>
        <div class="contact-value">benz@steland.com.au</div>
      </div>
    </div>

    <div class="contact-item">
      <div class="contact-icon">📍</div>
      <div>
        <div class="contact-label" data-zh="地址" data-en="Address">地址</div>
        <div class="contact-value">
          <a href="https://maps.google.com/?q=Level+7,+9+Help+Street,+Chatswood+NSW+2067" target="_blank" style="color: var(--gold-light); text-decoration: none;">
            Level 7, 9 Help Street<br>Chatswood NSW 2067
          </a>
        </div>
      </div>
    </div>

    <div class="contact-item">
      <div class="contact-icon">👤</div>
      <div>
        <div class="contact-label" data-zh="联系人" data-en="Contact">联系人</div>
        <div class="contact-value">Ben</div>
      </div>
    </div>

    <div class="contact-item">
      <div class="contact-icon">🏢</div>
      <div>
        <div class="contact-label" data-zh="公司" data-en="Company">公司</div>
        <div class="contact-value">Steland Construction</div>
      </div>
    </div>
  </div>

  <form class="contact-form" onsubmit="handleSubmit(event)">
    <div class="form-group">
      <label data-zh="您的姓名" data-en="Your Name">您的姓名</label>
      <input type="text" id="input-name" placeholder="Name" required>
    </div>
    <div class="form-group">
      <label data-zh="电子邮箱" data-en="Email Address">电子邮箱</label>
      <input type="email" placeholder="Email" required>
    </div>
    <div class="form-group">
      <label data-zh="服务类型" data-en="Service Type">服务类型</label>
      <select>
        <option value="" data-zh="请选择服务" data-en="Select a service">请选择服务</option>
        <option data-zh="室内装修" data-en="Interior Fitout">室内装修</option>
        <option data-zh="空间改建" data-en="Renovation">空间改建</option>
        <option data-zh="扩建加建" data-en="Extensions">扩建加建</option>
        <option data-zh="建筑翻新" data-en="Restoration">建筑翻新</option>
        <option data-zh="新建项目" data-en="New Build">新建项目</option>
      </select>
    </div>
    <div class="form-group">
      <label data-zh="项目详情" data-en="Project Details">项目详情</label>
      <textarea id="textarea-details" placeholder="请描述您的项目需求..."></textarea>
    </div>
    <button type="submit" class="btn-submit" data-zh="发送询问" data-en="Send Enquiry">发送询问</button>
  </form>
</section>

<footer>
  <span>© 2025 Steland Construction. All rights reserved.</span>
  <span data-zh="联系人：Ben &nbsp;|&nbsp; benz@steland.com.au" data-en="Contact: Ben &nbsp;|&nbsp; benz@steland.com.au">联系人：Ben &nbsp;|&nbsp; benz@steland.com.au</span>
</footer>

<script>
  // Scroll fade-in
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) e.target.classList.add('visible');
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));

  // ── Language switching ──
  let currentLang = 'zh';

  function setLang(lang) {
    currentLang = lang;
    document.getElementById('btn-zh').classList.toggle('active', lang === 'zh');
    document.getElementById('btn-en').classList.toggle('active', lang === 'en');
    document.documentElement.lang = lang === 'zh' ? 'zh' : 'en';

    // Update all elements with data-zh / data-en
    document.querySelectorAll('[data-zh][data-en]').forEach(el => {
      const val = el.getAttribute('data-' + lang);
      if (!val) return;
      // Elements that allow HTML (h1, h2 with <br><em> etc.)
      if (el.tagName === 'H1' || el.tagName === 'H2') {
        el.innerHTML = val;
      } else {
        el.textContent = val;
      }
    });

    // Textarea placeholder
    const ta = document.getElementById('textarea-details');
    if (ta) ta.placeholder = lang === 'zh' ? '请描述您的项目需求...' : 'Describe your project requirements...';

    // Name input placeholder
    const ni = document.getElementById('input-name');
    if (ni) ni.placeholder = lang === 'zh' ? '姓名' : 'Full name';
  }

  // Form submit
  function handleSubmit(e) {
    e.preventDefault();
    const btn = e.target.querySelector('.btn-submit');
    btn.textContent = currentLang === 'zh' ? '✓ 已发送！' : '✓ Sent!';
    btn.style.background = '#4a7c59';
    setTimeout(() => {
      btn.textContent = currentLang === 'zh' ? '发送询问' : 'Send Enquiry';
      btn.style.background = '';
      e.target.reset();
    }, 3000);
  }
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)
