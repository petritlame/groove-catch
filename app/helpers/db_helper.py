from app.database.connection import get_connection


def create_database():
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS videos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                video_id VARCHAR(255) DEFAULT NULL,
                playlist_id VARCHAR(255) DEFAULT NULL,
                playlist_name VARCHAR(255) DEFAULT NULL,
                url TEXT,
                is_downloaded tinyint(1) DEFAULT 0,
                UNIQUE (video_id)
            )
        ''')
        conn.commit()
        conn.close()


def save_videos_to_db(videos, playlist_name):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.executemany(
            """
            INSERT IGNORE INTO videos (video_id, playlist_id, playlist_name, url)
            VALUES (%s, %s, %s, %s)
            """,
            [(video['video_id'], video['playlist_id'], playlist_name, video['url']) for video in videos]
        )

        conn.commit()
        conn.close()


def get_videos_from_db():
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT url, video_id FROM videos WHERE is_downloaded = 0")
        rows = cursor.fetchall()  # Fetch all rows
        conn.close()

        # Convert rows to a list of dictionaries
        video_data = [{"url": row[0], "video_id": row[1]} for row in rows]
        return video_data

    return []


def update_video(video_id):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                """
                UPDATE videos SET is_downloaded = 1 WHERE video_id = %s
                """,
                (video_id,)  # Pass as a tuple
            )
            conn.commit()
        except Exception as e:
            print(f"Error updating video: {e}")
        finally:
            conn.close()


