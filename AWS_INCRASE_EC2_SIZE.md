🔁 PART 1: Resize EC2 Instance Type (CPU/RAM)
✅ Step 1: Stop the instance

AWS Console → EC2 → Instances

Select your instance

Click Instance state → Stop

Wait until status = Stopped

✅ Step 2: Change instance type

Select instance

Click Actions → Instance settings → Change instance type

Choose:

t3.medium


Click Apply

✅ Step 3: Start instance

Click Instance state → Start

Wait for running

👉 CPU + RAM upgraded safely ✅

💾 PART 2: Resize Disk (EBS Volume) — VERY IMPORTANT
✅ Step 4: Modify EBS volume

Go to:

EC2 → Volumes


Select attached volume

Click Actions → Modify volume

Change size:

40 GB


Volume type:

gp3


Click Modify

⚠️ This is ONLINE, no data loss.

✅ Step 5: Extend filesystem inside EC2 (MANDATORY)

SSH into EC2:

ssh -i your-key.pem ec2-user@<EC2_PUBLIC_IP>

🔹 Check disk
lsblk

🔹 Verify
df -h

🔄 PART 3: Restart Jenkins (Recommended)
sudo systemctl restart jenkins

🧠 PRO DEVOPS TIP

After resize:

sudo docker system prune -af


Step 1: Grow the partition (correct device)
sudo growpart /dev/nvme0n1 1

🔹 Step 2: Resize XFS filesystem (THIS IS THE KEY)
sudo xfs_growfs /