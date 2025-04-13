from loader import cursor, bot, scheduler, con
from script.parser import parser_update


async def recreate_tasks():
    
    try:
        cursor.execute("SELECT user_id, id_task, url, task_time FROM MyTable")
        users = cursor.fetchall() 

        for user in users:
            user_id, id_task, url, task_time = user

            try:
              
                job = scheduler.add_job(
                    parser_update,
                    trigger="date",  
                    run_date=task_time,  
                    args=[user_id, bot]  
                )

                cursor.execute(
                    "UPDATE MyTable SET id_task = %s WHERE user_id = %s",
                    (job.id, user_id)
                )
                con.commit()

            except Exception as job_error:
                print(f"Ошибка при добавлении задачи для пользователя {user_id}: {job_error}")

        print("Все задачи успешно пересозданы!")

    except Exception as e:
        print(f"Ошибка при пересоздании задач: {e}")
