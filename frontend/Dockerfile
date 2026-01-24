FROM node:20-alpine

WORKDIR /app

# Create non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Copy package files
COPY package*.json ./

# Change ownership BEFORE npm install
RUN chown -R appuser:appgroup /app

# Switch to non-root user
USER appuser

# Install dependencies as non-root user
RUN npm install

# Copy source code
COPY --chown=appuser:appgroup . .

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host"]

