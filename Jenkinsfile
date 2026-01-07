// 这是Python项目专用的Jenkins流水线配置文件
pipeline {
    // 选择任意可用的构建节点
    agent any

    // 配置环境：指定Python版本（需提前在Jenkins全局工具里配好Python，名称要和这里一致）
    environment {
        PYTHON = tool 'HXSH' // 替换为你Jenkins里配置的Python名称
        TEST_REPORT = 'test_report.xml' // 测试报告文件名
        EMAIL_TO = '870098425@qq.com' // 替换为接收报告的邮箱
    }

    // 构建阶段
    stages {
        // 1. 从GitHub拉取代码
        stage('拉取代码') {
            steps {
                echo "正在从GitHub拉取代码..."
                git(
                    url: 'https://github.com/liran870098425/HX.git', // 你的GitHub仓库地址
                    branch: 'main' // 你的代码分支
                )
            }
        }

        // 2. 安装Python项目依赖
        stage('安装依赖') {
            steps {
                echo "正在安装Python依赖包..."
                sh """
                    # 使用指定的Python版本安装requirements.txt里的依赖
                    ${PYTHON}/bin/pip install -r requirements.txt pytest
                """
            }
        }

        // 3. 运行测试用例+生成报告
        stage('运行测试+生成报告') {
            steps {
                echo "正在执行测试用例并生成报告..."
                sh """
                    # 用pytest运行tests目录下的用例，生成JUnit格式的报告（Jenkins可直接解析）
                    ${PYTHON}/bin/testcase/ --junitxml=${TEST_REPORT}
                """
            }
            // 不管测试成功/失败，都归档报告
            post {
                always {
                    echo "归档测试报告..."
                    junit(
                        allowEmptyResults: true, // 允许无测试结果（避免空报告报错）
                        testResults: "${TEST_REPORT}"
                    )
                }
            }
        }
    }

    // 构建完成后：发邮件通知结果
    post {
        success {
            echo "测试通过，发送成功邮件..."
            emailext(
                to: "${EMAIL_TO}",
                subject: "✅ Jenkins测试通知：${JOB_NAME}构建#${BUILD_NUMBER}成功",
                body: """
                    项目：${JOB_NAME}
                    构建号：${BUILD_NUMBER}
                    状态：测试全部通过
                    报告地址：${BUILD_URL}testReport/
                    构建日志：${BUILD_URL}console
                """
            )
        }
        failure {
            echo "测试失败，发送失败邮件..."
            emailext(
                to: "${EMAIL_TO}",
                subject: "❌ Jenkins测试通知：${JOB_NAME}构建#${BUILD_NUMBER}失败",
                body: """
                    项目：${JOB_NAME}
                    构建号：${BUILD_NUMBER}
                    状态：测试执行失败
                    报告地址：${BUILD_URL}testReport/
                    构建日志：${BUILD_URL}console
                """
            )
        }
    }
}