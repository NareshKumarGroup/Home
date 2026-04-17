---
layout: default
title: Molecular docking tutorial
permalink: /Moleculardocking/
sitemap: false
---

<section class="section docking-tutorial-section">
  <div class="container docking-tutorial-container">
    <h1 class="docking-tutorial-title">Molecular docking tutorial (Kumar group)</h1>

    <div class="docking-callout docking-callout-private" role="note">
      <p><strong>Lab members only.</strong> This page and the video are intended for <strong>Kumar group members</strong> only. We would appreciate it if you <strong>do not share</strong> the link or the video outside the laboratory.</p>
    </div>

    <p class="docking-tutorial-intro">
      You can <strong>watch the tutorial online at any time</strong> using the player below, or <strong>download the MP4</strong> to view offline when that suits you better.
    </p>

    <p class="docking-tutorial-body">
      This tutorial is meant to give you a <strong>basic introduction</strong> to how molecular docking is done on the <strong>modelling PC</strong>, using <em>Molecular Docking Explained | Protein-Ligand Docking | Schrödinger Software</em> as a reference. Please treat it as <strong>foundational knowledge</strong> rather than a complete workflow for every project.
    </p>

    <p class="docking-tutorial-body">
      In practice, <strong>each project has its own settings</strong>—for example different configurations, recommended grid boxes, and other choices that depend on your system. We <strong>recommend that you ask your mentor</strong> (someone working on the same project as you) for project-specific settings, and for <strong>further guidance or tutorials</strong> tailored to the receptor you are working with.
    </p>

    <p class="docking-tutorial-body">
      If you need <strong>additional information</strong>, please feel free to <strong>reach out to me</strong> or to any of the <strong>senior members</strong> in the lab; most of them are now comfortable operating the software and can help point you in the right direction.
    </p>

    {% assign docking_video = '/moleculardockingtutorial/molecular-docking-tutorial.mp4' %}

    <div class="docking-tutorial-actions">
      <a class="btn docking-download-btn" href="{{ site.baseurl }}{{ docking_video }}" download="molecular-docking-tutorial.mp4">
        Download video (MP4)
      </a>
    </div>

    <div class="docking-video-wrap">
      <video class="docking-video" controls playsinline preload="metadata">
        <source src="{{ site.baseurl }}{{ docking_video }}" type="video/mp4">
        Your browser does not support embedded video. Use the download link above.
      </video>
    </div>

    <p class="docking-tutorial-note">
      Bookmark this URL if you need to return to the page; it is not linked from the public site navigation.
    </p>
  </div>
</section>

<style>
.docking-tutorial-section {
  padding: 2.5rem 0 4rem;
}

.docking-tutorial-container {
  max-width: 960px;
}

.docking-tutorial-title {
  font-size: 1.85rem;
  color: #2c3e50;
  margin-bottom: 1rem;
  font-weight: 600;
}

.docking-callout {
  border-radius: 10px;
  padding: 1rem 1.25rem;
  margin-bottom: 1.75rem;
  line-height: 1.6;
  font-size: 0.98rem;
}

.docking-callout-private {
  background: #fffbeb;
  border: 1px solid #fcd34d;
  color: #78350f;
}

.docking-callout-private p {
  margin: 0;
}

.docking-tutorial-intro {
  font-size: 1.05rem;
  line-height: 1.65;
  color: #444;
  margin-bottom: 1.25rem;
}

.docking-tutorial-body {
  font-size: 1.02rem;
  line-height: 1.65;
  color: #444;
  margin-bottom: 1.25rem;
  text-align: justify;
}

.docking-tutorial-actions {
  margin: 2rem 0 1.5rem;
}

.docking-download-btn {
  display: inline-block;
  text-decoration: none;
}

.docking-video-wrap {
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
  background: #0f172a;
}

.docking-video {
  display: block;
  width: 100%;
  max-height: 85vh;
  margin: 0 auto;
}

.docking-tutorial-note {
  margin-top: 2rem;
  font-size: 0.9rem;
  line-height: 1.5;
  color: #64748b;
}
</style>
