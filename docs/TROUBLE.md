# Troubleshooting

First you must provide proper values in `application.env`.
Make sure to all values a correct. If you container does not start, see logs:

```bash
docker logs application
```

### application.env

If you see `TypeError` it means you forget to create `application.env` or 
the file does not contain the expected values. See **[Run](docs/RUN.md)** for 
instructions about these values.

### Connection errors

If you see `RuntimeError` in container logs this probably means you have
provided the wrong AWS_KEY and AWS_SECRET. Doublecheck it.

### Database error

If you see `HTTP 500` error during execution of `/secret` it means database
does not contain the expected value. Make sure that provided CODENAME is right.
