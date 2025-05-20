# Inner Radius Calculator - Web Version

This is a web version of the Inner Radius Calculator, designed to be hosted on Vercel.

## Local Development

1. Install the required packages:

```bash
pip install -r requirements.txt
```

2. Run the Flask development server:

```bash
python app.py
```

3. Open your browser and navigate to `http://localhost:5000`

## Deploying to Vercel

### Prerequisites

- Vercel account (create one at [vercel.com](https://vercel.com))
- Vercel CLI (Install with `npm i -g vercel`)

### Deployment Steps

1. Log in to Vercel from the command line:

```bash
vercel login
```

2. Deploy the application:

```bash
vercel
```

3. Follow the prompts to complete the deployment.

### Deploy with Git Integration

Alternatively, you can connect your GitHub repository to Vercel for automatic deployments:

1. Push this code to a GitHub repository
2. In Vercel dashboard, create a new project and import the repository
3. Configure the project settings (the defaults should work)
4. Deploy!

## How It Works

This application solves for the inner radius (ri) using numerical methods based on input values M, F, and outer radius (ro). The calculation logic is the same as the desktop version, but now accessible through a web interface.
