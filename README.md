# AutoPCB

Automated PCB design from JSON specs to KiCad projects.

## Features

- **Board as Code**: Upload JSON/netlist → get complete KiCad project
- **Auto-routing**: Fully routed PCB with DRC checking
- **3D Models**: STL enclosures for mechanical integration
- **Fab-ready**: Gerbers, drill files, BOM, PnP
- **Editable**: Not a black box - standard KiCad project

## Quick Start

```bash
# Upload spec
curl -X POST https://autopcb.mkechem.com/api/design \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d @spec.json

# Download results
curl -X GET https://autopcb.mkechem.com/api/design/abc123/download \
  -H "Authorization: Bearer YOUR_TOKEN"
```

## API

### POST /api/design

Upload a JSON spec for PCB design.

**Request Body:**
```json
{
  "components": [
    {"name": "U1", "value": "TL431", "footprint": "SOT23-5", "x": 0, "y": 0}
  ],
  "layers": 2,
  "trace_width": 0.2
}
```

**Response:**
```json
{
  "design_id": "abc123",
  "status": "processing",
  "download_url": "/api/design/abc123/download"
}
```

### GET /api/design/{id}/download

Download the complete KiCad project.

## Pricing

- **Free**: 1 credit (one board)
- **Pro**: $49.99/month - unlimited boards

## License

MIT License - feel free to use in your projects.

## Contributing

Pull requests welcome! See [CONTRIBUTING.md](CONTRIBUTING.md).

## Demo

Try it live: https://autopcb.mkechem.com

## Contact

- GitHub Issues: https://github.com/autopcb/autopcb/issues
- Website: https://autopcb.mkechem.com

---

**Note**: This is a demo repository. The full AutoPCB platform is available at https://autopcb.mkechem.com
