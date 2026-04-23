from app.models.database import get_db_connection

class Category:
    @staticmethod
    def get_all():
        """取得所有分類"""
        conn = get_db_connection()
        categories = conn.execute('SELECT * FROM categories ORDER BY type, name').fetchall()
        conn.close()
        return [dict(row) for row in categories]

    @staticmethod
    def get_by_type(cat_type):
        """根據類型(income/expense)取得分類"""
        conn = get_db_connection()
        categories = conn.execute('SELECT * FROM categories WHERE type = ? ORDER BY name', (cat_type,)).fetchall()
        conn.close()
        return [dict(row) for row in categories]

    @staticmethod
    def get_by_id(category_id):
        """根據 ID 取得單一分類"""
        conn = get_db_connection()
        category = conn.execute('SELECT * FROM categories WHERE id = ?', (category_id,)).fetchone()
        conn.close()
        return dict(category) if category else None

    @staticmethod
    def create(name, cat_type):
        """新增分類"""
        conn = get_db_connection()
        cursor = conn.execute('INSERT INTO categories (name, type) VALUES (?, ?)', (name, cat_type))
        conn.commit()
        new_id = cursor.lastrowid
        conn.close()
        return new_id

    @staticmethod
    def update(category_id, name, cat_type):
        """更新分類"""
        conn = get_db_connection()
        conn.execute('UPDATE categories SET name = ?, type = ? WHERE id = ?', (name, cat_type, category_id))
        conn.commit()
        conn.close()
        return True

    @staticmethod
    def delete(category_id):
        """刪除分類"""
        conn = get_db_connection()
        # 注意：實務上若已有 record 使用此 category_id，直接刪除會違反 FK 或造成資料遺失
        conn.execute('DELETE FROM categories WHERE id = ?', (category_id,))
        conn.commit()
        conn.close()
        return True
