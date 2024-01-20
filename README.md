# Setting Up Django and React with NGINX and Gunicorn on Ubuntu server- Troubleshooting Guide

1. **NGINX Symbolic Link Error:**
   - **Problem:** When creating a symbolic link for NGINX configuration, I encounter a "File exists" error.
   - **Solution:** Removed the existing symbolic link before creating a new one.
     ```bash
     sudo rm /etc/nginx/sites-enabled/demo
     sudo ln -s /etc/nginx/sites-available/demo /etc/nginx/sites-enabled
     ```

2. **502 Bad Gateway Error:**
   - **Problem:** After configuring Gunicorn and NGINX, I encounter a "502 Bad Gateway" error.
   - **Solution:** Check Gunicorn logs for errors and ensure Gunicorn is running, and ran it.

3. **NGINX Permissions Error:**
   - **Problem:** permission errors when trying to access static files.
   - **Solution:** Adjust the permissions for static files to ensure NGINX can read them.
     ```bash
     chmod -R 755 /path/to/static
     ```

4. **Gunicorn Unit Not Found:**
   - **Problem:** Gunicorn service unit not found when trying to start.
   - **Solution:** Create a Gunicorn service file and enable it.
     ```ini
     # Example Gunicorn Service File
     [Unit]
     Description=Gunicorn daemon for demo project
     After=network.target

     [Service]
     User=root
     Group=root
     WorkingDirectory=/root/icode/demo
     ExecStart=/root/icode/venv/bin/gunicorn --workers=3 --bind unix:/root/icode/demo.sock demo.wsgi:application

     [Install]
     WantedBy=multi-user.target
     ```
     ```bash
     sudo systemctl enable gunicorn_demo.service
     sudo systemctl start gunicorn_demo.service
     ```


5. **404 Error for React App:**
   - **Problem:** React app returns a 404 error for routes other than the home page.
   - **Solution:** Adjust NGINX configuration for React routing.
     ```bash
     location /react/ {
         alias /var/www/build/;
         try_files $uri $uri/ /react/index.html;
     }
     ```

6. **NGINX Admin Panel Access Issue:**
   - **Problem:** NGINX routes requests to the Django admin panel incorrectly.
   - **Solution:** Check NGINX configuration to ensure correct routing for Django admin.
     ```bash
     location /admin/ {
         proxy_pass http://127.0.0.1:8000/admin/;
         proxy_set_header Host $host;
         proxy_set_header X-Real-IP $remote_addr;
         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
         proxy_set_header X-Forwarded-Proto $scheme;
     }
     ```

