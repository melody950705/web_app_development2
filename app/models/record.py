from app.models.database import get_db_connection

class Record:
    @staticmethod
    def get_all():
        """取得所有收支紀錄，並關聯分類名稱，依日期遞減排序"""
        conn = get_db_connection()
        query = '''
            SELECT r.*, c.name as category_name 
            FROM records r
            LEFT JOIN categories c ON r.category_id = c.id
            ORDER BY r.date DESC, r.id DESC
        '''
        records = conn.execute(query).fetchall()
        conn.close()
        return [dict(row) for row in records]

    @staticmethod
    def get_by_id(record_id):
        """根據 ID 取得單筆收支紀錄"""
        conn = get_db_connection()
        query = '''
            SELECT r.*, c.name as category_name 
            FROM records r
            LEFT JOIN categories c ON r.category_id = c.id
            WHERE r.id = ?
        '''
        record = conn.execute(query, (record_id,)).fetchone()
        conn.close()
        return dict(record) if record else None

    @staticmethod
    def create(date, amount, rec_type, category_id, description=''):
        """新增收支紀錄"""
        conn = get_db_connection()
        cursor = conn.execute(
            'INSERT INTO records (date, amount, type, description, category_id) VALUES (?, ?, ?, ?, ?)',
            (date, amount, rec_type, description, category_id)
        )
        conn.commit()
        new_id = cursor.lastrowid
        conn.close()
        return new_id

    @staticmethod
    def update(record_id, date, amount, rec_type, category_id, description=''):
        """更新收支紀錄"""
        conn = get_db_connection()
        conn.execute(
            '''UPDATE records 
               SET date = ?, amount = ?, type = ?, description = ?, category_id = ? 
               WHERE id = ?''',
            (date, amount, rec_type, description, category_id, record_id)
        )
        conn.commit()
        conn.close()
        return True

    @staticmethod
    def delete(record_id):
        """刪除收支紀錄"""
        conn = get_db_connection()
        conn.execute('DELETE FROM records WHERE id = ?', (record_id,))
        conn.commit()
        conn.close()
        return True

    @staticmethod
    def get_balance_summary():
        """計算總收入、總支出與總餘額"""
        conn = get_db_connection()
        query = '''
            SELECT 
                SUM(CASE WHEN type = 'income' THEN amount ELSE 0 END) as total_income,
                SUM(CASE WHEN type = 'expense' THEN amount ELSE 0 END) as total_expense
            FROM records
        '''
        result = conn.execute(query).fetchone()
        conn.close()
        
        income = result['total_income'] or 0
        expense = result['total_expense'] or 0
        balance = income - expense
        
        return {
            'total_income': income,
            'total_expense': expense,
            'balance': balance
        }
