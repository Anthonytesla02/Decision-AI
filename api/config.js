export default function handler(req, res) {
  // Set CORS headers
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  // Only allow GET requests
  if (req.method !== 'GET') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  // Return the public configuration
  res.status(200).json({
    PAYSTACK_PUBLIC_KEY: process.env.PAYSTACK_PUBLIC_KEY || null,
    // Never expose secret key to client
    // PAYSTACK_SECRET_KEY is only used server-side
  });
}