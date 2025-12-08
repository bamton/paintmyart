# Paint My Art - Coloring Pages Landing Page

A high-converting landing page for selling digital coloring pages for children ages 5-9.

## Features

- **Premium Design**: Black background with bold white typography for a sophisticated, high-converting aesthetic
- **Direct Copy**: No-fluff messaging focused on screen-free activities and child development
- **Interactive Gallery**: Hover effects and print functionality for sample pages
- **Sample Testing**: Users can print samples to test quality before purchasing
- **Bonus Content**: Includes word search puzzles as an additional value
- **Responsive Design**: Optimized for all devices
- **Payment Integration**: Direct Stripe checkout integration

## What's Included

- 75 high-quality coloring pages
- Word search puzzle collection
- Winter holiday themed pages
- Fantasy and adventure themes
- Everyday fun themes

## Technical Details

- Built with pure HTML, CSS, and JavaScript
- No dependencies or frameworks required
- Mobile-first responsive design
- Smooth animations and parallax effects
- Print-optimized CSS for sample pages

## File Structure

```
paintmyartapp/
├── index.html          # Main landing page
├── styles.css          # All styles
├── script.js           # Interactive functionality
├── samples/            # Sample images and word search
│   ├── *.png          # Sample coloring pages
│   └── word-search.png # Word search puzzle
└── README.md           # This file
```

## Payment Integration

The site integrates with Stripe for secure payments:
- Live checkout link: https://buy.stripe.com/dRm3cvfRS1xYfnmdkX7Re00
- All CTAs redirect to Stripe checkout
- Opens in new tab for better UX

## Usage

1. Simply open `index.html` in a web browser
2. No server required - static site
3. For production, deploy to any static hosting service

## Customization

- Update pricing in `index.html` (currently $9.00)
- Replace Stripe link with your own
- Update images in `samples/` directory
- Modify colors in `styles.css` (currently black/white theme)

## Deployment

Can be deployed to:
- Netlify
- Vercel
- GitHub Pages
- Any static hosting service