// Preview carousel
const previewItems = document.querySelectorAll('.preview-item');
const dots = document.querySelectorAll('.dot');
let currentIndex = 0;

function showSlide(index) {
    previewItems.forEach(item => item.classList.remove('active'));
    dots.forEach(dot => dot.classList.remove('active'));

    previewItems[index].classList.add('active');
    dots[index].classList.add('active');
}

function nextSlide() {
    currentIndex = (currentIndex + 1) % previewItems.length;
    showSlide(currentIndex);
}

// Auto-rotate preview every 4 seconds
setInterval(nextSlide, 4000);

// Click to change slide
dots.forEach((dot, index) => {
    dot.addEventListener('click', () => {
        currentIndex = index;
        showSlide(currentIndex);
    });
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Animate elements on scroll
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe all sections
document.querySelectorAll('section').forEach(section => {
    section.style.opacity = '0';
    section.style.transform = 'translateY(30px)';
    section.style.transition = 'opacity 0.8s ease, transform 0.8s ease';
    observer.observe(section);
});

// Counter animation for stats
function animateCounter(element, target) {
    const duration = 2000;
    const step = target / (duration / 16);
    let current = 0;

    const timer = setInterval(() => {
        current += step;
        if (current >= target) {
            current = target;
            clearInterval(timer);
        }

        if (element.dataset.format === 'limit') {
            element.textContent = Math.floor(current).toLocaleString();
        } else {
            element.textContent = Math.floor(current);
        }
    }, 16);
}

// Initialize counters when visible
const statNumbers = document.querySelectorAll('.number[data-target]');
const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting && !entry.target.dataset.animated) {
            entry.target.dataset.animated = 'true';
            const target = parseInt(entry.target.dataset.target);
            animateCounter(entry.target, target);
        }
    });
}, { threshold: 0.5 });

statNumbers.forEach(number => {
    counterObserver.observe(number);
});

// Countdown timer removed

// Purchase notifications removed

// Add hover effects to gallery items
document.querySelectorAll('.gallery-item').forEach(item => {
    item.addEventListener('mouseenter', function() {
        this.style.transform = 'scale(1.05) translateY(-5px)';
    });

    item.addEventListener('mouseleave', function() {
        this.style.transform = 'scale(1) translateY(0)';
    });
});

// Add parallax effect to hero section
window.addEventListener('scroll', () => {
    const scrolled = window.pageYOffset;
    const hero = document.querySelector('.hero');
    const heroContent = document.querySelector('.hero-text');

    if (hero && heroContent) {
        heroContent.style.transform = `translateY(${scrolled * 0.5}px)`;
        heroContent.style.opacity = 1 - scrolled / 600;
    }
});

// Track scroll depth for analytics (placeholder)
let maxScroll = 0;
window.addEventListener('scroll', () => {
    const scrollPercent = (window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100;
    maxScroll = Math.max(maxScroll, scrollPercent);

    // Log scroll milestones (in production, send to analytics)
    if (maxScroll > 25 && maxScroll < 26) {
        console.log('User scrolled 25%');
    } else if (maxScroll > 50 && maxScroll < 51) {
        console.log('User scrolled 50%');
    } else if (maxScroll > 75 && maxScroll < 76) {
        console.log('User scrolled 75%');
    } else if (maxScroll > 95 && maxScroll < 96) {
        console.log('User reached bottom');
    }
});

// Print image function
function printImage(imageSrc, imageName) {
    // Create a hidden print area
    const printArea = document.createElement('div');
    printArea.className = 'print-area';

    printArea.innerHTML = `
        <div class="print-content">
            <img src="${imageSrc}" alt="${imageName}">
        </div>
    `;

    document.body.appendChild(printArea);

    // Wait for image to load, then print
    const img = printArea.querySelector('img');
    img.onload = function() {
        window.print();
        // Remove print area after printing
        setTimeout(() => {
            printArea.remove();
        }, 100);
    };
}


// Add cursor trail effect for premium feel
let mouseTimer;
document.addEventListener('mousemove', (e) => {
    clearTimeout(mouseTimer);

    const trail = document.createElement('div');
    trail.className = 'cursor-trail';
    trail.style.left = e.clientX + 'px';
    trail.style.top = e.clientY + 'px';

    document.body.appendChild(trail);

    mouseTimer = setTimeout(() => {
        trail.remove();
    }, 500);
});

// Add cursor trail styles
if (!document.querySelector('#cursor-styles')) {
    const style = document.createElement('style');
    style.id = 'cursor-styles';
    style.textContent = `
        .cursor-trail {
            position: fixed;
            width: 4px;
            height: 4px;
            background: rgba(255, 255, 255, 0.5);
            border-radius: 50%;
            pointer-events: none;
            z-index: 9998;
            animation: fadeOut 0.5s ease forwards;
        }
        @keyframes fadeOut {
            to {
                opacity: 0;
                transform: scale(0);
            }
        }
    `;
    document.head.appendChild(style);
}