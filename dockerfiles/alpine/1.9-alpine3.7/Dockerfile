# Go image from which to get timezone files
FROM golang:1.9-alpine3.7 as go

# Bare os image
FROM alpine:3.7
WORKDIR /usr/local/go/lib/time/
COPY from=go /usr/local/go/lib/time/zoneinfo.zip .
