---
layout: default
title: Tools
permalink: /tools/
---

<section class="section tools-section">
    <div class="container">
        <div class="section-title">
            <h2>In-house Tools</h2>
        </div>

        <p class="tools-intro">
            In-house tools for research and teaching will be listed here.
        </p>
    </div>
</section>

<style>
.tools-section {
    padding-top: 1rem;
}

.tools-intro {
    max-width: 760px;
    margin: -1.5rem auto 2.5rem;
    text-align: center;
    color: #444;
    font-size: 1.05rem;
    line-height: 1.65;
}

.tools-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 360px));
    gap: 1.25rem;
}

.tool-tile {
    display: flex;
    flex-direction: column;
    min-height: 220px;
    padding: 1.5rem 1.4rem 1.25rem;
    background: #fff;
    border: 1px solid #e6e4f2;
    border-radius: 12px;
    box-shadow: 0 2px 12px rgba(109, 95, 217, 0.08);
    color: inherit;
    text-decoration: none;
    transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
}

.tool-tile:hover {
    transform: translateY(-3px);
    border-color: #c4b5fd;
    box-shadow: 0 8px 24px rgba(109, 95, 217, 0.16);
    text-decoration: none;
}

.tool-tile-kicker {
    color: #6d5fd9;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 0.55rem;
}

.tool-tile h3 {
    font-size: 1.35rem;
    color: #2c3e50;
    margin-bottom: 0.6rem;
}

.tool-tile p {
    color: #444;
    line-height: 1.6;
    margin: 0 0 1.25rem;
    flex: 1;
}

.tool-tile-action {
    align-self: flex-start;
    color: #fff;
    background: linear-gradient(135deg, #6d5fd9 0%, #818cf9 25%, #a78bfa 50%, #8b5cf6 75%, #7c3aed 100%);
    border-radius: 4px;
    padding: 0.45rem 0.85rem;
    font-size: 0.9rem;
    font-weight: 500;
}
</style>
