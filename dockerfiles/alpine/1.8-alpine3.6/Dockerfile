# Go image from which to get timezone files
FROM golang:1.8-alpine3.6 as go

# Bare os image
FROM alpine:3.6
WORKDIR /usr/local/go/lib/time/
COPY from=go /usr/local/go/lib/time/zoneinfo.zip .
