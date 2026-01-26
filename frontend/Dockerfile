FROM node:20-alpine

# Set working directory
WORKDIR /app

# Create non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Copy package files
COPY package*.json ./

# Fix permissions before install
RUN chown -R appuser:appgroup /app

# Switch to non-root user
USER appuser

# Install dependencies
RUN npm install

# Copy source code
COPY --chown=appuser:appgroup . .

# Expose Vite dev port
EXPOSE 5173

# Start Vite dev server
CMD ["npm", "run", "dev", "--", "--host"]
